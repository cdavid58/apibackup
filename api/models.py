from django.db import models
from django.utils.crypto import get_random_string
from base64 import b64decode
import os,base64


class BackUp_Payroll(models.Model):
	company = models.IntegerField()
	payroll_document = models.TextField(default="")
	month = models.CharField(max_length = 15,default = "")
	anio = models.IntegerField(default = 0)

class BackUp_PDFS(models.Model):
	company = models.IntegerField()
	pdf = models.TextField(unique = True)
	type_pdf = models.IntegerField(default = 1)
	number = models.IntegerField(default = 1)
	prefix = models.CharField(max_length=10,default = "")
	token = models.CharField(max_length = 96,default = "")
	pk_company = models.IntegerField(default=1)
	pk_invoice = models.IntegerField(default = 1)

	def CreatePDF(self,name_pdf):
		path_dir = './media/company/'+str(self.company)+'/'
		if not os.path.exists(path_dir):
			os.mkdir(path_dir)
		
		print(path_dir)

		bytes = b64decode(self.pdf.encode('ascii'), validate=True)
		print(path_dir+'/'+name_pdf+'.pdf')
		f = open(path_dir+'/'+name_pdf+'.pdf', 'wb')
		f.write(bytes)
		f.close()

	def Send_Email(self):
		_type = "FES-"
		if self.type_pdf == 1:
			_type = "POS-"
		path_dir = './media/company/'+str(self.company)+'/'+_type+str(self.prefix)+str(self.number)+'.pdf'
		print(path_dir)
		if not os.path.exists(path_dir):
			self.CreatePDF(_type+str(self.prefix)+str(self.number)) 
		import smtplib
		import requests
		import json
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText
		from email.mime.base import MIMEBase
		from email import encoders
		remitente = 'facturacionelectronica387@gmail.com'
		destinatarios = ["carlosdelaguila917@gmail.com"]
		asunto = 'Aceptación de factura N° '#+str(factura.prefijo)+str(factura.numero)
		html = """
		<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
			<html xmlns="http://www.w3.org/1999/xhtml">
			 
			<head>
			  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
			  <title>Factura electronica</title>
			  <style type="text/css">
			  body {margin: 0; padding: 0; min-width: 100%!important;}
			  img {height: auto;}
			  .content {width: 100%; max-width: 600px;}
			  .header {padding: 40px 30px 20px 30px;}
			  .innerpadding {padding: 30px 30px 30px 30px;}
			  .borderbottom {border-bottom: 1px solid #f2eeed;}
			  .subhead {font-size: 15px; color: #ffffff; font-family: sans-serif; letter-spacing: 10px;}
			  .h1, .h2, .bodycopy {color: #153643; font-family: sans-serif;}
			  .h1 {font-size: 33px; line-height: 38px; font-weight: bold;}
			  .h2 {padding: 0 0 15px 0; font-size: 24px; line-height: 28px; font-weight: bold;}
			  .bodycopy {font-size: 16px; line-height: 22px;}
			  .button {text-align: center; font-size: 18px; font-family: sans-serif; font-weight: bold; padding: 0 30px 0 30px;}
			  .button a {color: #ffffff; text-decoration: none;}
			  .footer {padding: 20px 30px 15px 30px;}
			  .footercopy {font-family: sans-serif; font-size: 14px; color: #ffffff;}
			  .footercopy a {color: #ffffff; text-decoration: underline;}

			  @media only screen and (max-width: 550px), screen and (max-device-width: 550px) {
			  body[yahoo] .hide {display: none!important;}
			  body[yahoo] .buttonwrapper {background-color: transparent!important;}
			  body[yahoo] .button {padding: 0px!important;}
			  body[yahoo] .button a {background-color: #e05443; padding: 15px 15px 13px!important;}
			  body[yahoo] .unsubscribe {display: block; margin-top: 20px; padding: 10px 50px; background: #2f3942; border-radius: 5px; text-decoration: none!important; font-weight: bold;}
			  }

			  </style>
			</head>

			<body yahoo bgcolor="#f6f8f1">
			<table width="100%" bgcolor="#f6f8f1" border="0" cellpadding="0" cellspacing="0">
			<tr>
			  <td>
			    <!--[if (gte mso 9)|(IE)]>
			      <table width="600" align="center" cellpadding="0" cellspacing="0" border="0">
			        <tr>
			          <td>
			    <![endif]-->     
			    <table bgcolor="#ffffff" class="content" align="center" cellpadding="0" cellspacing="0" border="0">
			      <tr>
			        <td style=" background-image: linear-gradient(to left top, #0db9f8, #0790be, #0c6988, #0f4456, #0c222a);" class="header">
			          <table width="70" align="left" border="0" cellpadding="0" cellspacing="0">  
			            <tr>
			              <td height="70" style="padding: 0 20px 20px 0;">
			                <img class="fix" src="https://scontent.feoh1-1.fna.fbcdn.net/v/t39.30808-6/236831317_373363691048746_6124884787829342845_n.jpg?_nc_cat=109&ccb=1-5&_nc_sid=09cbfe&_nc_eui2=AeHC2pd9PxQIaMrlI6hGR7_KM4Mr_Q2yPQkzgyv9DbI9CTyKT7YfoHSHHmKHZ07ufKLotsaDLkQ49Do25yRYbBsP&_nc_ohc=s0gnbPs5NWcAX-vebaw&_nc_ht=scontent.feoh1-1.fna&oh=00_AT9FfGCvn1UA0mqFqunFbxN3WqHc0WaGX5k2U8ysTk3lxw&oe=62509A4E" width="70" height="70" border="0" alt="" />
			              </td>
			            </tr>
			          </table>
			          <!--[if (gte mso 9)|(IE)]>
			            <table width="425" align="left" cellpadding="0" cellspacing="0" border="0">
			              <tr>
			                <td>
			          <![endif]-->
			          <table class="col425" align="left" border="0" cellpadding="0" cellspacing="0" style="width: 100%; max-width: 425px;">  
			            <tr>
			              <td height="70">
			                <table width="100%" border="0" cellspacing="0" cellpadding="0">
			                  <!-- <tr>
			                    <td class="subhead" style="padding: 0 0 0 3px;">
			                      <span style="color: white;">$(company_name)</span>
			                    </td>
			                  </tr> -->
			                  <tr>
			                    <td class="h1" style="padding: 5px 0 0 0;">
			                     <span style="color: white;">$(company_name)</span>
			                    </td>
			                  </tr>
			                </table>
			              </td>
			            </tr>
			          </table>
			          <!--[if (gte mso 9)|(IE)]>
			                </td>
			              </tr>
			          </table>
			          <![endif]-->
			        </td>
			      </tr>
			      <tr>
			        <td class="innerpadding borderbottom">
			          <table width="100%" border="0" cellspacing="0" cellpadding="0">
			            <tr>
			              <td class="h2">
			               Hola,$(client) !
			              </td>
			            </tr>
			            <tr>
			              <td class="bodycopy">
			                Mediante la presente, le informamos del envío de la factura electrónica de venta N° $(number_invoice).<br>
			                Cualquier duda o inquietud nos puede informar por medio de algunas de las opciones que le presentamos por este medio.
							<br>
							<br>
							<span style="font-size: 25px;font-weight: bold;">NOTA:&nbsp;</span><span style="font-size:18px;">ANTES DE SELECCIONAR CUALQUIER OPCIÓN POR FAVOR VERIFIQUE BIEN LOS DATOS DE SU FACTURA</span>
			              </td>
			            </tr>
			          </table>
			        </td>
			      </tr>
			      <tr>
			        <td class="innerpadding borderbottom">
			          <!-- <table width="115" align="left" border="0" cellpadding="0" cellspacing="0">  
			            <tr>
			              <td height="115" style="padding: 0 20px 20px 0;">
			                <img class="fix" src="http://theriosoft.com/static/vendors/itemsHome/facturaPdf.png" width="115" height="115" border="0" alt="" />
			              </td>
			            </tr>
			          </table> -->
			          <!--[if (gte mso 9)|(IE)]>
			            <table width="380" align="left" cellpadding="0" cellspacing="0" border="0">
			              <tr>
			                <td>
			          <![endif]-->
			          <table class="col380" align="left" border="0" cellpadding="0" cellspacing="0" style="width: 100%; max-width: 380px;">  
			            <tr>
			              <td>
			                <table width="100%" border="0" cellspacing="0" cellpadding="0">
			               
			                  <tr>
			                    <td style="padding: 20px 0 0 0;">
			                      <table class="buttonwrapper" style="background-image: linear-gradient(to left bottom, #0db9f8, #0790be, #0c6988, #0f4456, #0c222a);" border="0" cellspacing="0" cellpadding="0">
			                        <tr>
			                          <td class="button" height="45">
			                            <a href="http://34.125.180.32/invoice/acceptance/$(token)/$(pk_company)/$(number_invoice)" target="_blank">Aceptar</a>
			                          </td>
			                          <td>&nbsp;&nbsp;&nbsp;</td>
			                          <td class="button" height="45">
			                            <a href="http://34.125.180.32/invoice/rejection/$(token)/$(pk_company)/$(number_invoice)" target="_blank">Rechazar</a>
			                          </td>
			                         
			                        
			                        </tr>
			                        
			                         
			                        </tr>
			                      </table>



			                    </td>
			                  </tr>
			                </table>
			              </td>
			            </tr>
			          </table>
			          <!--[if (gte mso 9)|(IE)]>
			                </td>
			              </tr>
			          </table>
			          <![endif]-->
			        </td>
			      </tr>
			      
			     
			    </table>
			    <!--[if (gte mso 9)|(IE)]>
			          </td>
			        </tr>
			    </table>
			    <![endif]-->
			    </td>
			  </tr>
			</table>

			</body>
			</html>
		"""

		html = html.replace("$(company_name)","Evansoft")
		html = html.replace("$(client)","Buggy")
		html = html.replace("$(token)",str(self.token))
		html = html.replace("$(number_invoice)",str(self.pk_invoice))
		html = html.replace("$(pk_company)",str(self.pk_company))


		ruta_adjunto = path_dir
		nombre_adjunto = _type+str(self.prefix)+str(self.number)
		mensaje = MIMEMultipart()

		mensaje['From'] = remitente
		mensaje['To'] = ", ".join(destinatarios)
		mensaje['Subject'] = asunto
		mensaje.attach(MIMEText(html,'html'))


		archivo_adjunto = open(ruta_adjunto, 'rb')

		adjunto_MIME = MIMEBase('application', 'octet-stream')
		adjunto_MIME.set_payload((archivo_adjunto).read())
		encoders.encode_base64(adjunto_MIME)
		adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)

		mensaje.attach(adjunto_MIME)
		sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
		sesion_smtp.starttls()
		texto = mensaje.as_string()
		usuario = "facturacionelectronica387"
		clave = "megatron12#$"
		sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
		sesion_smtp.starttls()
		texto = mensaje.as_string()
		remitente = usuario
		sesion_smtp.login(usuario,clave)
		sesion_smtp.sendmail(remitente, destinatarios, texto)
		sesion_smtp.quit()



