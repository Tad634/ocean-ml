# to do
import sys
example_date = sys.argv[1]
# vectorq.exec:
vectorq = open("vectorq.exec",'w')
vectorq.write("#!/bin/csh\n\n")
vectorq,write("set indir = /Users/brownscholar/Desktop")
vectorq.write("set dir = ./test/\n")
vectorq.write("set fileinfo = {$dir}info_pr.dat\n")
vectorq.write("set filedh =  {$indir}/file_dynamic_height/dh_"+example_date+".gr\n")
vectorq.write("set filest =  {$indir}/file_density/density_"+example_date+".gr\n")
vectorq.write("set filestm = {$dir}ss1_st0.dat\n")
vectorq.write("set filequ =  {$dir}ss1a2qu.gr\n")
vectorq.write("set fileqv =  {$dir}ss1a2qv.gr\n")
vectorq.write("set fileqdi = {$dir}ss1a2qdi.gr\n")
vectorq.write("./vectorq.exe << !\n")
vectorq.write("'$fileinfo'	#>>>>>Escribe info file info.dat:\n")
vectorq.write("'$filedh'	#>>>>>Escribe fichero de altura Dinamica:\n")
vectorq.write("'$filest'	#>>>>>Escribe fichero de densidad:\n")
vectorq.write("'$filestm'	#>>>>>Escribe fichero de densidad promedio:\n")
vectorq.write("'$filequ'	#>>>>>Escribe fichero Qu:\n")
vectorq.write("'$fileqv'	#>>>>>Escribe fichero Qv:\n")
vectorq.write("'$fileqdi'	#>>>>>Escribe fichero Qdi:\n")
vectorq.close()

#omegainv.exec:
omegainv = open("omegainv.exec",'w')

omegainv.write("#!/bin/csh\n")
omegainv.write("set dir = ./test/\n")
omegainv.write("set fileinfo = {$dir}info_pr.dat\n")
omegainv.write("set filestm = {$dir}ss1_st0.dat\n")
omegainv.write("set fileqdi = {$dir}ss1a2qdi.gr\n")
omegainv.write("set filew =   {$dir}ss1a2ww.gr\n")

omegainv.write("./omegainv.exe << !\n")
omegainv.write("'$fileinfo' 	#>>>>>Escribe info file info.dat:\n")
omegainv.write("'$fileqdi' 	#>>>>>Escribe fichero de Div Q:\n")
omegainv.write("'$filestm'   	#>>>>>Escribe fichero de densidad promedio:\n")
omegainv.write("'ominput.dat'  #>>>>>Escribe fichero parametros (ominput.dat):\n")
omegainv.write("'$filew'	#>>>>>Escribe fichero Salida W:\n")
omegainv.write("!\n")
omegainv.close()
