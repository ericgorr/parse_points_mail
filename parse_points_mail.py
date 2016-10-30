import os
import time
import email
import pprint
import re
import webbrowser

from bs4 import BeautifulSoup

POINTS_MAIL_PATH = "/Users/ericg/Desktop/points_mail"

files = os.listdir( POINTS_MAIL_PATH )

for file in files:
    if file.startswith( ".DS_Store" ) is False:
        messagePath = os.path.join( POINTS_MAIL_PATH, file )

        with open( messagePath, "r" ) as fp:
            message = email.message_from_file( fp )

            for part in message.walk():
                if part.get_content_type() == "text/html":
                    htmlContent = part.as_string()
                    soup        = BeautifulSoup( htmlContent, 'html.parser' )
                    results = soup.find_all( 'b' )
                    for result in results:
                         if result.string.startswith( "Receive" ):
                            pattern     = "Receive [0-9]* Points\."
                            patternRE   = re.compile( pattern )
                            match       = patternRE.match( result.string )

                            if match is not None:
                                spanParent = result.parent.parent

                                links = spanParent.find_all( 'a' )

                                if len( links ) == 1:
                                    theLink = links[0][ 'href' ]

                                    if theLink is not None:
                                        webbrowser.open( theLink, autoraise = False )
                                        print( file )










