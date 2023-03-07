
# Coded BY Awham 
# Channel : @jj_8tl
# instagram : jj_8t

try:
	import sys,threading,requests,random
	from os import system
except Exception as Wl:
	print(" MISSING LIB , ",Wl)
	input()
	sys.exit()

system('clear')
print('''
                  _                     
     /\          | |                    
    /  \__      _| |__   __ _ _ __ ___  
   / /\ \ \ /\ / / '_ \ / _` | '_ ` _ \ 
  / ____ \ V  V /| | | | (_| | | | | | |
 /_/    \_\_/\_/ |_| |_|\__,_|_| |_| |_|
 
 https://t.me/jj_8tl
''')

class Awham:
	
	def __init__(self):
			
		self.length = int(input('User length : '))
		print('')
		self.Error = 0
		self.Good = 0
		self.aa = True
		for i in range (10):
			threading.Thread (target=self.jj_8t).start()
			
	def jj_8t(self):
		
		Aw = 'qwertyuioplmknjbhvgcfxdzsa'
		while self.aa:
			Awham = ''.join((random.choice(Aw) for e in range(self.length)))
			url = "https://github.com/signup_check/username"
			headers = {
				"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
				"Referer":"https://github.com/signup?return_to=https%3A%2F%2Fgithub.com%2Fsignup%3Fref_cta%3DSign%2Bup%26ref_loc%3Dheader%2Blogged%2Bout%26ref_page%3D%252F%26source%3Dheader-home&source=login",
				"Cookie":"_gh_sess=No0kcxG%2B%2FKA%2FZJ2p8TS2WQc1gHArt0NYBP9aXwyN77r9mH6aUiy0azpUbHECaQrlAEsPE43rZNcA0P1oVNd8YbTsth%2BzX0ri5ZbawhYTv9si%2BJzwPRIjiaCi8Q1v2R0Y82a1hyZL4r69OlZDJF%2F1iNKqHbuIIfKZFITuBh%2FjLuY%2FLP31Cv7AxG66DJjnDvChmNZAU%2FRm3ywX9CjE4yWR7OcHvGJlOWvhlnBa2OWUpR2PH%2FY5nGLs7i1nD3MyqMdNXT9nXODKbomprUfiJcqFMkDjPfRnUdy7r0f8cg87va4aJWPx--GlpfJG%2FOF4MejHpQ--SHnJVTmnE2ohtSrJDU3FCQ%3D%3D; tz=Asia%2FRiyadh; preferred_color_mode=dark; _device_id=68e186d0c76bfcf6036f3d9c9fbd3631; _octo=GH1.1.867718780.1661539884; logged_in=no"
				}
			files = {
				'authenticity_token':(None, 'gLWL+5hrWUjrrOZfsZ2E6+0i9ctNBAoom9ylUfu7phTmNM5ln+rOtdqCuN3pkXh0piwVYYhctyNoLZHSCbzRdA=='),
				'value':(None, Awham),
				}
			r = requests.post(url,headers=headers,files=files)
			if 'is available.' in r.text:
				self.Good+=1
				open('Awham.txt','a').write(Awham+'\n')
			
			else:
				self.Error+=1
			
			print(f'\rError : {self.Error} | Good : {self.Good}',end='')
			
Awham()
