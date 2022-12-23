from dataclasses import field, fields
from distutils.command.upload import upload
from enum import auto
from lib2to3.pgen2 import grammar
from pyexpat import model
from re import M
from unicodedata import decomposition
from unittest import mock
import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import  Mtumiaji, Mwanachama, Dharura, Mkopo, Ratibayavikao, Umojawetu, Madeni
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations




class MwanachamaType(DjangoObjectType):
    class Meta:
        model = Mwanachama
        fields = '__all__'
        # fields = ("mtumiaji_ID", "mwanachama_phone", "mwanachama_cheo", "mwanachama_jinsia")
    
class MtumiajiType(DjangoObjectType):
    class Meta:
        model = Mtumiaji
        fields = '__all__'
        
        
class DharuraType(DjangoObjectType):
    class Meta:
        model = Dharura
        fields = '__all__'
        
class MkopoType(DjangoObjectType):
    class Meta:
        model = Mkopo
        fields = '__all__'
        
        
class MadeniType(DjangoObjectType):
    class Meta:
        model = Madeni
        fields = '__all__'
                
class RatibayavikaoType(DjangoObjectType):
    class Meta:
        model = Ratibayavikao
        fields = '__all__'
        
class UmojawetuType(DjangoObjectType):
    class Meta:
        model = Umojawetu 
        fields = '__all__'                               
            
    
class Query(MeQuery, graphene.ObjectType):
    all_wanachama = DjangoListField(MwanachamaType)
    mwanachama = graphene.Field(MwanachamaType, id=graphene.Int())
    
    def resolve_all_wanachama(root, info):
        return Mwanachama.objects.all()
    
    def resolve_mwanachama(root, info, id):
        return Mwanachama.objects.get(pk=id)
    
    all_dharura = DjangoListField(DharuraType)
    dharura = graphene.Field(DharuraType, id=graphene.Int())
    
    def resolve_all_dharura(root, info):
        return Dharura.objects.all()
    
    def resolve_dharura(root, info, id):
        return Dharura.objects.get(pk=id)
    
    all_mkopo = DjangoListField(MkopoType)
    mkopo = graphene.Field(MkopoType, id=graphene.Int())

    
    def resolve_all_mkopo(root, info):
        return Mkopo.objects.all()
    
    def resolve_mkopo(root, info, id):
        return Mkopo.objects.get(pk=id)
    
    all_madeni = DjangoListField(MadeniType)
    
    def resolve_all_madeni(root, info):
        return Madeni.objects.all()
    
    all_ratibayavikao = DjangoListField(RatibayavikaoType)
    ratibayavikao = graphene.Field(DharuraType, id=graphene.Int())
    
    def resolve_all_ratibayavikao(root,info):
        return Ratibayavikao.objects.all()
    
    def resolve_ratibayavikao(root, info, id):
        return Ratibayavikao.objects.get(pk=id)
    
    
    all_umojawetu = DjangoListField(UmojawetuType)
    
    def resolve_all_umojawetu(root, info):
        return Umojawetu.objects.all()
    
    

class CreateMwanachama(graphene.Mutation):
    mwanachama = graphene.Field(MwanachamaType)
    class Arguments:
        mwanachama_jina = graphene.String(required=True)
        mwanachama_phone = graphene.String(required=True)
        mwanachama_cheo = graphene.Int()
        mwanachama_jinsia = graphene.Int()
        # pichayamwanachama = upload()
 

    def mutate(self, info, mwanachama_jina, mwanachama_phone, mwanachama_cheo, mwanachama_jinsia):
        mtu = Mwanachama(mwanachama_jina=mwanachama_jina ,mwanachama_cheo=mwanachama_cheo, mwanachama_phone=mwanachama_phone, mwanachama_jinsia=mwanachama_jinsia)
        # mtumiaji = Mtumiaji.objects.get(id=mtumiajiID)
        # mtu.mtumiajiID = mtumiaji
        mtu.save()
        return CreateMwanachama(mwanachama=mtu)   
    
    
class UpdateMwanachama(graphene.Mutation):
    mwanachama = graphene.Field(MwanachamaType)
    
    class Arguments:
        id = graphene.Int()
        mwanachama_jina= graphene.String(required=True)
        mwanachama_cheo = graphene.Int()
        mwanachama_jinsia = graphene.Int()
        mwanachama_phone = graphene.String(required=True)
        pichayamwanachama = graphene.String()
        
        
    def mutate(root, info, id, mwanachama_jina, mwanachama_phone, mwanachama_cheo, mwanachama_jinsia):
        mwana = Mwanachama.objects.get(id=id)
        mwana.mwanachama_cheo = mwanachama_cheo
        mwana.mwanachama_jina = mwanachama_jina
        mwana.mwanachama_jinsia = mwanachama_jinsia
        mwana.mwanachama_phone = mwanachama_phone
        # mtu = Mwanachama(mwanachama_jina=mwanachama_jina ,mwanachama_cheo=mwanachama_cheo, mwanachama_phone=mwanachama_phone, mwanachama_jinsia=mwanachama_jinsia)
        # mtumiaji = Mtumiaji.objects.get(id=mtumiajiID)
        # mtu.mtumiajiID = mtumiaji
        mwana.save()
        return UpdateMwanachama(mwanachama=mwana)        
    
class DeleteMwanachama(graphene.Mutation):
    mwanachama = graphene.Field(MwanachamaType)
    
    class Arguments:
        id = graphene.ID()
        
    def mutate(root, info, id):
        mwana = Mwanachama.objects.get(id=id)
        mwana.delete()
        return DeleteMwanachama(mwanachama=mwana)    

# ******************************************************************************************

class CreateDharura(graphene.Mutation):
    dharura = graphene.Field(DharuraType)
    class Arguments:
        mwanachamaID = graphene.Int()
        sababuyadharura = graphene.String(required=True)
        tareheyadharura = graphene.DateTime()
        sikuyadharurakuombwa = graphene.DateTime()
        
    def mutate(root, info, mwanachamaID, sababuyadharura, tareheyadharura, sikuyadharurakuombwa):
        dhar = Dharura(sababuyadharura=sababuyadharura,tareheyadharura=tareheyadharura,sikuyadharurakuombwa=sikuyadharurakuombwa)
        mwanachama = Mwanachama.objects.get(id=mwanachamaID)
        dhar.mwanachamaID = mwanachama
        dhar.save()
        return CreateDharura(dharura=dhar)    
    
    
class UpdateDharura(graphene.Mutation):
    dharura = graphene.Field(DharuraType)
    class Arguments:
        id = graphene.Int()
        mtumiajiID = graphene.Int()
        sababuyadharura = graphene.String(required=True)
        tareheyadharura = graphene.DateTime()
        sikuyadharurakuombwa = graphene.DateTime()

    def mutate(root, info, id, mtumiajiID, sababuyadharura, tareheyadharura, sikuyadharurakuombwa):
        dhar = Dharura.objects.get(id=id)
        dhar.mtumiajiID = mtumiajiID
        dhar.sababuyadharura = sababuyadharura
        dhar.tareheyadharura = tareheyadharura
        dhar.sikuyadharurakuombwa = sikuyadharurakuombwa
        dhar.save()
        return UpdateDharura(dharura=dhar)
    
class DeleteDharura(graphene.Mutation):
    dharura = graphene.Field(DharuraType)
    
    class Arguments:
        id =  graphene.Int()
        
    def mutate(root, info, id):
        dhar = Dharura.objects.get(id=id)
        dhar.delete()
        return DeleteDharura(dharura = dhar)       
#***************************************************************************************************************    
class CreateMkopo(graphene.Mutation):
    mkopo = graphene.Field(MkopoType)
    class Arguments:
        mwanachamaID = graphene.Int()
        kiasichamkopo = graphene.String()
        tareheyakuombwa = graphene.Date()
        tareheyakurudishwa = graphene.Date()
        
    def mutate(root, info, mwanachamaID, kiasichamkopo, tareheyakuombwa, tareheyakurudishwa):
        mko = Mkopo(kiasichamkopo=kiasichamkopo, tareheyakuombwa=tareheyakuombwa, tareheyakurudishwa=tareheyakurudishwa)
        mwanachama = Mwanachama.objects.get(id=mwanachamaID)
        mko.mwanachamaID = mwanachama
        mko.save()
        return CreateMkopo(mkopo=mko)   
    
class UpdateMkopo(graphene.Mutation):
    mkopo = graphene.Field(MkopoType)
    
    class Arguments:
        id = graphene.ID()
        mwanachamaID = graphene.Int()
        kiasichamkopo = graphene.String()
        tareheyakuombwa = graphene.Date()
        tareheyakurudishwa = graphene.Date()
        
    def mutate(root, info, id, mwanachamaID, kiasichamkopo, tareheyakuombwa, tareheyakurudishwa):
        mko = Mkopo.objects.get(id=id)
        mwanachama = Mwanachama.objects.get(pk=mwanachamaID)
        mko.mwanachamaID = mwanachama
        mko.kiasichamkopo = kiasichamkopo
        mko.tareheyakuombwa = tareheyakuombwa
        mko.tareheyakurudishwa = tareheyakurudishwa  
        
        # denilako = kiasichamkopo
        # kiasikilichowekwa = 
        # x = "decomp"
        # if kiasichamkopo == x:
        #     kiasichamkopo = kiasichamkopo - x
        #     print(kiasichamkopo)
            
        mko.save()
        return UpdateMkopo(mkopo = mko)    
                    

# class UpdateMkopo(graphene.Mutation):
#     mkopo = graphene.Field(MkopoType)
#     class Arguments:
#         id = graphene.Int()
#         mwanachamaID = graphene.String()
#         kiasichamkopo = graphene.String()
#         tareheyakuombwa = graphene.Date()
#         tareheyakurudishwa = graphene.Date()
        
#     def mutate(root, info, id, mwanchamaID, kiasichamkopo,, tareheyakuombwa, tareheyakurudisha):
#         if kiasichamkopo == "Borrow More":
#             kiasikipya = mkopowazamani + kiasichamkopo              

class CreateMadeni(graphene.Mutation):
    madeni = graphene.Field(MadeniType)
    # kiasikilichowekwa = int(input("weka pesaa"))
    
    class Arguments:
        mwanachamaID = graphene.Int()
        mkopoID = graphene.Int()
        kiasikilichowekwa = graphene.Int()
        tareheyakuwekapesa = graphene.Date()
        kiasichamkopokilichobaki = graphene.Int()
        
    def mutate(root, info, mwanachamaID, mkopoID, kiasikilichowekwa, tareheyakuwekapesa, kiasichamkopokilichobaki):
        mwanachama = Mwanachama.objects.get(id=mwanachamaID)
        mkopo = Mkopo.objects.get(id=mkopoID)
        mad = Madeni(kiasichamkopokilichobaki=kiasichamkopokilichobaki, kiasikilichowekwa=kiasikilichowekwa,tareheyakuwekapesa=tareheyakuwekapesa)
        mad.mwanachamaID = mwanachama 
        mad.mkopoID = mkopo
        # denilako = mkopo
        # kiasikilichowekwa = int(input("weka pesa: "))
        if kiasikilichowekwa == mkopo:
            mkopo = mkopo - kiasikilichowekwa
            if kiasikilichowekwa < mkopo:
                mkopo = mkopo - kiasikilichowekwa    
        else:
            return mkopo
                
        mad.save()
        return CreateMadeni(madeni = mad)    
# *****************************************************************************************************

class CreateRatiba(graphene.Mutation): 
    ratibayavikao = graphene.Field(RatibayavikaoType)
    class Arguments:
        kikaoid= graphene.Int()
        kikaoagenda = graphene.String()
        sikuyakikao = graphene.String()
        mudawakikao = graphene.Time()
        mahalipakikao = graphene.String()
        tareheyakikao = graphene.Date()
        
        
    def mutate(root, info, kikaoid, kikaoagenda, sikuyakikao, mudawakikao, mahalipakikao, tareheyakikao):
        rat = Ratibayavikao(kikaoid=kikaoid, kikaoagenda=kikaoagenda, sikuyakikao=sikuyakikao, mudawakikao=mudawakikao, mahalipakikao=mahalipakikao, tareheyakikao=tareheyakikao)
        rat.save()
        return CreateRatiba(ratibayavikao = rat)    
        
        
class UpdateRatiba(graphene.Mutation):
    ratiba = graphene.Field(RatibayavikaoType)
    class Arguments:
        id = graphene.Int()
        # kikaoid= graphene.Int()
        kikaoagenda = graphene.String()
        sikuyakikao = graphene.String()
        mudawakikao = graphene.Time()
        mahalipakikao = graphene.String()
        tareheyakikao = graphene.Date()  
        
        
    def  mutate(root, info, id,  kikaoagenda, sikuyakikao, mudawakikao, mahalipakikao, tareheyakikao):
        rat = Ratibayavikao.objects.get(id=id)
        # rat.kikaoid = kikaoid
        rat.kikaoagenda = kikaoagenda  
        rat.sikuyakikao = sikuyakikao
        rat.mudawakikao = mudawakikao
        rat.mahalipakikao = mahalipakikao
        rat.tareheyakikao = tareheyakikao
        rat.save()
        return UpdateRatiba(ratiba=rat)       


class DeleteRatiba(graphene.Mutation):
    ratiba = graphene.Field(RatibayavikaoType)
    class Arguments:
        id = graphene.Int()
        
    def mutate(root, info, id):
        rat = Ratibayavikao.objects.get(id=id)
        rat.delete()
        return DeleteRatiba(ratiba= rat)  
    
    
      
#********************************************************************************************* 
class CreateUmojawetu(graphene.Mutation):
    umojawetu = graphene.Field(UmojawetuType)
    
    class Arguments:
        mwanachamajina = graphene.String()
        taarifahusika = graphene.String()
        sikuyatukio = graphene.Date()
        
    def mutate(root, info, mwanachamajina, taarifahusika, sikuyatukio):
        umoja = Umojawetu(mwanachamajina=mwanachamajina, taarifahusika=taarifahusika, sikuyatukio=sikuyatukio)
        umoja.save()
        return CreateUmojawetu(umojawetu = umoja)    

class UpdateUmojawetu(graphene.Mutation):
    umojawetu = graphene.Field(UmojawetuType)
    
    class Arguments:
        id = graphene.Int()
        mwanachamajina = graphene.String()
        taarifahusika = graphene.String()
        sikuyatukio = graphene.Date()
        
    def mutate(root, info, id, mwanachamajina, taarifahusika, sikuyatukio ):
        umoja = Umojawetu.objects.get(pk=id)
        umoja.mwanachamajina = mwanachamajina
        umoja.taarifahusika = taarifahusika
        umoja.sikuyatukio = sikuyatukio
        umoja.save()
        return UpdateUmojawetu(umojawetu = umoja)    

class AuthMutation(graphene.ObjectType):
    register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    update_account = mutations.UpdateAccount.Field()
    send_secondary_email_activation = mutations.SendSecondaryEmailActivation.Field()
    verify_secondary_email = mutations.VerifySecondaryEmail.Field()
    swap_emails = mutations.SwapEmails.Field()

    # django-graphql-jwt inheritances
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()
    
    
         
class Mutation(AuthMutation, graphene.ObjectType):
    create_mwanachama = CreateMwanachama.Field()
    update_mwanachama = UpdateMwanachama.Field()
    delete_mwanachama = DeleteMwanachama.Field()
    
    
    create_dharura = CreateDharura.Field()
    update_dharura = UpdateDharura.Field()
    delete_dharura = DeleteDharura.Field()
    
    create_mkopo = CreateMkopo.Field()
    update_mkopo = UpdateMkopo.Field()
    
    create_ratiba = CreateRatiba.Field()
    update_ratiba = UpdateRatiba.Field()
    delete_ratiba = DeleteRatiba.Field()
    
    create_madeni = CreateMadeni.Field()
    
    create_umoja = CreateUmojawetu.Field()
    update_umoja = UpdateUmojawetu.Field()
    
    
    
    
    
       
schema = graphene.Schema(query=Query, mutation=Mutation)       



# query {
#   allWanachama{
#     id
#     mwanachamaCheo
#     mwanachamaPhone
#     mwanachamaJinsia
#   }
# }

# query {
#   mwanachama(id: 2) {
#     mtumiajiID{
#       id
#     }
#     mwanachamaCheo
#     mwanachamaPhone
#     mwanachamaJinsia
#     pichayamwanachama
#   }
# }




# mutation {
#   createMwanachama(mtumiajiID:"1", mwanachamaCheo:2, mwanachamaJinsia:0, mwanachamaPhone: "+2550755348431"){
#     mwanachama{
#       id
#       mwanachamaCheo
#       mwanachamaJinsia
#       mwanachamaPhone
#     }
#   }
# }





# mutation {
#   register(email: "email1@email.com",
#   username: "@user1",
#   password1: "testpass12345",
#   password2: "testpass12345") {
#     success
#     errors
#     token
#   }
# }



# mutation {
#   verifyAccount(token: "eyJ1c2VybmFtZSI6IkB1c2VyMSIsImFjdGlvbiI6ImFjdGl2YXRpb24ifQ:1okq0F:MRk7X4kG2z7JAL-0Mg2LSlz-AmfGKb6Zl2JxK_aZDrg"){
#     success
#     errors
#   }
# }

# mutation {
#   tokenAuth(password:"testpass12345",
#   email: "email1@email.com") {
#     success
#     errors
#     token
#     user{
#       id
#       verified
#     }
#   }
# }



# query {
#   me {
#     id
#     verified
#     username
#   }
# }


# mutation {
#   createDharura(mwanachamaID:2, sababuyadharura:"MSIBA", sikuyadharurakuombwa:"2022-10-19T20:02:50.200273+00:00",tareheyadharura: "2022-10-19T20:02:47+00:00"){
#     dharura{
#       mwanachamaID{
#         id
#       }
#      sababuyadharura
#      sikuyadharurakuombwa
#      tareheyadharura 
#     }
#   }
# }

# mutation{
#   updateDharura(id:1, mtumiajiID:1,sababuyadharura:"MSIBA",sikuyadharurakuombwa:"2022-10-19T20:02:50.200273+00:00",tareheyadharura: "2022-10-19T20:02:47+00:00"){
#     dharura{
#       mwanachamaID{
#         id
#       }
#      sababuyadharura
#      sikuyadharurakuombwa
#      tareheyadharura 
#     }
#   }
# }



# query{
#   allDharura{
#     id
#     sababuyadharura
#     tareheyadharura
#     sikuyadharurakuombwa
#   }
# }

