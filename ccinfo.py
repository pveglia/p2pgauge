"""
This file contains a big hash whose elements are hashes.
Keys for the outer hash are country codes.
Inner hashes contain information on the country as the complete name,
continent, lat & long, timezone offset respect to GMT.

The hash is called ccinfo

USE
from ccinfo import ccinfo 
"""

ccinfo = {
           'bd' : {
                     'country' : 'Bangladesh',
                     'lat' : '24.0000',
                     'continent' : 'Asia',
                     'lon' : '90.0000',
                     'tz' : '21600'
                   },
           'ne' : {
                     'country' : 'Nigeria',
                     'lat' : '10.0000',
                     'continent' : 'Africa',
                     'lon' : '8.0000',
                     'tz' : '3600'
                   },
           'ki' : {
                     'country' : 'Kiribati',
                     'lat' : '1.4167',
                     'continent' : 'Oceania',
                     'lon' : '173.0000',
                     'tz' : '43200'
                   },
           'mc' : {
                     'country' : 'Monaco',
                     'lat' : '43.7333',
                     'continent' : 'Europe',
                     'lon' : '7.4000',
                     'tz' : '3600'
                   },
           'mm' : {
                     'country' : 'Myanmar (Burma)',
                     'lat' : 'NaN',
                     'continent' : 'Asia',
                     'lon' : 'NaN',
                     'tz' : '23400'
                   },
           'tr' : {
                     'country' : 'Turkey',
                     'lat' : '39.0000',
                     'continent' : 'Asia',
                     'lon' : '35.0000',
                     'tz' : '7200'
                   },
           'fx' : {
                     'country' : 'France',
                     'lat' : '46.0000',
                     'continent' : 'Europe',
                     'lon' : '2.0000',
                     'tz' : '3600'
                   },
           'gl' : {
                     'country' : 'Greenland',
                     'lat' : '72.0000',
                     'continent' : 'Europe',
                     'lon' : '-40.0000',
                     'tz' : '-10800'
                   },
           'hn' : {
                     'country' : 'Honduras',
                     'lat' : '15.0000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-86.5000',
                     'tz' : '-21600'
                   },
           'my' : {
                     'country' : 'Malaysia',
                     'lat' : '2.5000',
                     'continent' : 'Asia',
                     'lon' : '112.5000',
                     'tz' : '28800'
                   },
           'ug' : {
                     'country' : 'Uganda',
                     'lat' : '1.0000',
                     'continent' : 'Africa',
                     'lon' : '32.0000',
                     'tz' : '10800'
                   },
           'nu' : {
                     'country' : 'Niue Island',
                     'lat' : '-19.0333',
                     'continent' : 'Oceania',
                     'lon' : '-169.8667',
                     'tz' : '-39600'
                   },
           'ci' : {
                     'country' : 'Ivory Coast',
                     'lat' : '7.5469',
                     'continent' : 'Africa',
                     'lon' : '-5.5471',
                     'tz' : '0'
                   },
           'ro' : {
                     'country' : 'Romania',
                     'lat' : '46.0000',
                     'continent' : 'Europe',
                     'lon' : '25.0000',
                     'tz' : '7200'
                   },
           'dk' : {
                     'country' : 'Denmark',
                     'lat' : '56.0000',
                     'continent' : 'Europe',
                     'lon' : '10.0000',
                     'tz' : '3600'
                   },
           'tn' : {
                     'country' : 'Tunisia',
                     'lat' : '34.0000',
                     'continent' : 'Africa',
                     'lon' : '9.0000',
                     'tz' : '3600'
                   },
           'co' : {
                     'country' : 'Columbia',
                     'lat' : 'NaN',
                     'continent' : 'SouthAmerica',
                     'lon' : 'NaN',
                     'tz' : '-18000'
                   },
           'nc' : {
                     'country' : 'New Caledonia',
                     'lat' : '-21.5000',
                     'continent' : 'Oceania',
                     'lon' : '165.5000',
                     'tz' : '39600'
                   },
           'rw' : {
                     'country' : 'Rwanda',
                     'lat' : '-2.0000',
                     'continent' : 'Africa',
                     'lon' : '30.0000',
                     'tz' : '7200'
                   },
           'br' : {
                     'country' : 'Brazil',
                     'lat' : '-10.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-55.0000',
                     'tz' : '-14400'
                   },
           'bo' : {
                     'country' : 'Bolivia',
                     'lat' : '-17.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-65.0000',
                     'tz' : '-14400'
                   },
           'cy' : {
                     'country' : 'Cyprus',
                     'lat' : '35.0000',
                     'continent' : 'Europe',
                     'lon' : '33.0000',
                     'tz' : '7200'
                   },
           'st' : {
                     'country' : 'Sao Tome & Principe',
                     'lat' : '1',
                     'continent' : 'Africa',
                     'lon' : '7',
                     'tz' : '0'
                   },
           'ck' : {
                     'country' : 'Cook Islands',
                     'lat' : '-21.2333',
                     'continent' : 'Oceania',
                     'lon' : '-159.7667',
                     'tz' : '-3600'
                   },
           'tc' : {
                     'country' : 'Turks & Caicos Islands',
                     'lat' : '21.75',
                     'continent' : 'NorthAmerica',
                     'lon' : '-71.5833',
                     'tz' : '-18000'
                   },
           'ke' : {
                     'country' : 'Kenya',
                     'lat' : '1.0000',
                     'continent' : 'Africa',
                     'lon' : '38.0000',
                     'tz' : '10800'
                   },
           'mo' : {
                     'country' : 'Macau',
                     'lat' : '22.1667',
                     'continent' : 'Asia',
                     'lon' : '113.5500',
                     'tz' : '28800'
                   },
           'gq' : {
                     'country' : 'Equatorial Guinea',
                     'lat' : '2.0000',
                     'continent' : 'Africa',
                     'lon' : '10.0000',
                     'tz' : '3600'
                   },
           'ge' : {
                     'country' : 'Georgia',
                     'lat' : '42.0000',
                     'continent' : 'Europe',
                     'lon' : '43.5000',
                     'tz' : '14400'
                   },
           'km' : {
                     'country' : 'Comoros Island',
                     'lat' : '-12.1667',
                     'continent' : 'Africa',
                     'lon' : '44.2500',
                     'tz' : '10800'
                   },
           'bf' : {
                     'country' : 'Burkina Faso',
                     'lat' : '13.0000',
                     'continent' : 'Oceania',
                     'lon' : '-2.0000',
                     'tz' : '0'
                   },
           'ao' : {
                     'country' : 'Angola',
                     'lat' : '-12.5000',
                     'continent' : 'Africa',
                     'lon' : '18.5000',
                     'tz' : '3600'
                   },
           'gr' : {
                     'country' : 'Greece',
                     'lat' : '39.0000',
                     'continent' : 'Europe',
                     'lon' : '22.0000',
                     'tz' : '7200'
                   },
           'ls' : {
                     'country' : 'Lesotho',
                     'lat' : '-29.5000',
                     'continent' : 'Africa',
                     'lon' : '28.5000',
                     'tz' : '7200'
                   },
           'mv' : {
                     'country' : 'Maldives Republic',
                     'lat' : '3.2500',
                     'continent' : 'Asia',
                     'lon' : '73.0000',
                     'tz' : '18000'
                   },
           'is' : {
                     'country' : 'Iceland',
                     'lat' : '65.0000',
                     'continent' : 'Europe',
                     'lon' : '-18.0000',
                     'tz' : '0'
                   },
           'tm' : {
                     'country' : 'Turkmenistan',
                     'lat' : '40.0000',
                     'continent' : 'Asia',
                     'lon' : '60.0000',
                     'tz' : '18000'
                   },
           'jm' : {
                     'country' : 'Jamaica',
                     'lat' : '18.2500',
                     'continent' : 'NorthAmerica',
                     'lon' : '-77.5000',
                     'tz' : '-18000'
                   },
           'ky' : {
                     'country' : 'Cayman Islands',
                     'lat' : '19.5000',
                     'continent' : 'Oceania',
                     'lon' : '-80.5000',
                     'tz' : '-18000'
                   },
           'mt' : {
                     'country' : 'Malta',
                     'lat' : '35.8333',
                     'continent' : 'Europe',
                     'lon' : '14.5833',
                     'tz' : '3600'
                   },
           'pg' : {
                     'country' : 'Papua New Guinea',
                     'lat' : '-6.0000',
                     'continent' : 'Oceania',
                     'lon' : '147.0000',
                     'tz' : '3600'
                   },
           'ga' : {
                     'country' : 'Gabon',
                     'lat' : '-1.0000',
                     'continent' : 'Africa',
                     'lon' : '11.7500',
                     'tz' : '3600'
                   },
           'gi' : {
                     'country' : 'Gibraltar',
                     'lat' : '36.1333',
                     'continent' : 'Europe',
                     'lon' : '-5.3500',
                     'tz' : '3600'
                   },
           'la' : {
                     'country' : 'Laos',
                     'lat' : '18.0000',
                     'continent' : 'Asia',
                     'lon' : '105.0000',
                     'tz' : '25200'
                   },
           'bh' : {
                     'country' : 'Bahrain',
                     'lat' : '26.0000',
                     'continent' : 'Asia',
                     'lon' : '50.5500',
                     'tz' : '10800'
                   },
           'ms' : {
                     'country' : 'Montserrat',
                     'lat' : '16.7500',
                     'continent' : 'NorthAmerica',
                     'lon' : '-62.2000',
                     'tz' : '-14400'
                   },
           'gb' : {
                     'country' : 'UK',
                     'lat' : '55.40342',
                     'continent' : 'Europe',
                     'lon' : '-3.21145',
                     'tz' : '0'
                   },
           'bt' : {
                     'country' : 'Bhutan',
                     'lat' : '27.5000',
                     'continent' : 'Asia',
                     'lon' : '90.5000',
                     'tz' : '19800'
                   },
           'sv' : {
                     'country' : 'El Salvador',
                     'lat' : '13.8333',
                     'continent' : 'NorthAmerica',
                     'lon' : '-88.9167',
                     'tz' : '-21600'
                   },
           'it' : {
                     'country' : 'Italy',
                     'lat' : '42.8333',
                     'continent' : 'Europe',
                     'lon' : '12.8333',
                     'tz' : '3600'
                   },
           'wf' : {
                     'country' : 'Wallis & Futuna Islands',
                     'lat' : '-13.3',
                     'continent' : 'Oceania',
                     'lon' : '-176.2',
                     'tz' : '43200'
                   },
           'mq' : {
                     'country' : 'Martinique',
                     'lat' : '14.6667',
                     'continent' : 'NorthAmerica',
                     'lon' : '-61.0000',
                     'tz' : '-14400'
                   },
           'hu' : {
                     'country' : 'Hungary',
                     'lat' : '47.0000',
                     'continent' : 'Europe',
                     'lon' : '20.0000',
                     'tz' : '3600'
                   },
           'sb' : {
                     'country' : 'Solomon Islands',
                     'lat' : '-8.0000',
                     'continent' : 'Oceania',
                     'lon' : '159.0000',
                     'tz' : '39600'
                   },
           'za' : {
                     'country' : 'South Africa',
                     'lat' : '-29.0000',
                     'continent' : 'Africa',
                     'lon' : '24.0000',
                     'tz' : '7200'
                   },
           'ly' : {
                     'country' : 'Libya',
                     'lat' : '25.0000',
                     'continent' : 'Africa',
                     'lon' : '17.0000',
                     'tz' : '7200'
                   },
           'ng' : {
                     'country' : 'Nigeria',
                     'lat' : '10.0000',
                     'continent' : 'Africa',
                     'lon' : '8.0000',
                     'tz' : '3600'
                   },
           'se' : {
                     'country' : 'Sweden',
                     'lat' : '62.0000',
                     'continent' : 'Europe',
                     'lon' : '15.0000',
                     'tz' : '3600'
                   },
           'gt' : {
                     'country' : 'Guatemala',
                     'lat' : '15.5000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-90.2500',
                     'tz' : '-21600'
                   },
           'uy' : {
                     'country' : 'Uruguay',
                     'lat' : '-33.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-56.0000',
                     'tz' : '-10800'
                   },
           'ai' : {
                     'country' : 'Anguilla',
                     'lat' : '18.2500',
                     'continent' : 'NorthAmerica',
                     'lon' : '-63.1667',
                     'tz' : '14400'
                   },
           'iq' : {
                     'country' : 'Iraq',
                     'lat' : '33.0000',
                     'continent' : 'Asia',
                     'lon' : '44.0000',
                     'tz' : '10800'
                   },
           'lu' : {
                     'country' : 'Luxembourg',
                     'lat' : '49.7500',
                     'continent' : 'Europe',
                     'lon' : '6.1667',
                     'tz' : '3600'
                   },
           'na' : {
                     'country' : 'Namibia',
                     'lat' : '-22.0000',
                     'continent' : 'Africa',
                     'lon' : '17.0000',
                     'tz' : '7200'
                   },
           've' : {
                     'country' : 'Venezuela',
                     'lat' : '8.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-66.0000',
                     'tz' : '-14400'
                   },
           'il' : {
                     'country' : 'Israel',
                     'lat' : '31.5000',
                     'continent' : 'Asia',
                     'lon' : '34.7500',
                     'tz' : '7200'
                   },
           'pt' : {
                     'country' : 'Portugal',
                     'lat' : '39.5000',
                     'continent' : 'Europe',
                     'lon' : '-8.0000',
                     'tz' : '3600'
                   },
           'mh' : {
                     'country' : 'Marshall Islands',
                     'lat' : '9.0000',
                     'continent' : 'Oceania',
                     'lon' : '168.0000',
                     'tz' : '3600'
                   },
           'eg' : {
                     'country' : 'Egypt',
                     'lat' : '27.0000',
                     'continent' : 'Africa',
                     'lon' : '30.0000',
                     'tz' : '7200'
                   },
           'ba' : {
                     'country' : 'Bosnia',
                     'lat' : '44',
                     'continent' : 'Europe',
                     'lon' : '18',
                     'tz' : '3600'
                   },
           'ph' : {
                     'country' : 'Philippines',
                     'lat' : '13.0000',
                     'continent' : 'Asia',
                     'lon' : '122.0000',
                     'tz' : '28800'
                   },
           'kg' : {
                     'country' : 'Kyrgyzstan',
                     'lat' : '41.0000',
                     'continent' : 'Asia',
                     'lon' : '75.0000',
                     'tz' : '21600'
                   },
           'pf' : {
                     'country' : 'French Polynesia',
                     'lat' : '-15.0000',
                     'continent' : 'Oceania',
                     'lon' : '-140.0000',
                     'tz' : '-3600'
                   },
           'no' : {
                     'country' : 'Norway',
                     'lat' : '62.0000',
                     'continent' : 'Europe',
                     'lon' : '10.0000',
                     'tz' : '3600'
                   },
           'lv' : {
                     'country' : 'latvia',
                     'lat' : '57.0000',
                     'continent' : 'Europe',
                     'lon' : '25.0000',
                     'tz' : '10800'
                   },
           'fr' : {
                     'country' : 'France',
                     'lat' : '46.0000',
                     'continent' : 'Europe',
                     'lon' : '2.0000',
                     'tz' : '3600'
                   },
           'kz' : {
                     'country' : 'Kazakhstan',
                     'lat' : '48.0000',
                     'continent' : 'Asia',
                     'lon' : '68.0000',
                     'tz' : '21600'
                   },
           'ma' : {
                     'country' : 'Morocco',
                     'lat' : '32.0000',
                     'continent' : 'Africa',
                     'lon' : '-5.0000',
                     'tz' : '0'
                   },
           'in' : {
                     'country' : 'India',
                     'lat' : '20.0000',
                     'continent' : 'Asia',
                     'lon' : '77.0000',
                     'tz' : '18000.5'
                   },
           'id' : {
                     'country' : 'Indonesia',
                     'lat' : '-5.0000',
                     'continent' : 'Asia',
                     'lon' : '120.0000',
                     'tz' : '25200'
                   },
           'sr' : {
                     'country' : 'Surinam',
                     'lat' : '4.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-56.0000',
                     'tz' : '-12600'
                   },
           'si' : {
                     'country' : 'Slovenia',
                     'lat' : '46.1167',
                     'continent' : 'Europe',
                     'lon' : '14.8167',
                     'tz' : '3600'
                   },
           're' : {
                     'country' : 'Reunion Island',
                     'lat' : '-21.1000',
                     'continent' : 'Oceania',
                     'lon' : '55.6000',
                     'tz' : '14400'
                   },
           'om' : {
                     'country' : 'Oman',
                     'lat' : '21.0000',
                     'continent' : 'Asia',
                     'lon' : '57.0000',
                     'tz' : '14400'
                   },
           'by' : {
                     'country' : 'Belarus',
                     'lat' : '53.0000',
                     'continent' : 'Europe',
                     'lon' : '28.0000',
                     'tz' : '10800'
                   },
           'fi' : {
                     'country' : 'Finland',
                     'lat' : '64.0000',
                     'continent' : 'Europe',
                     'lon' : '26.0000',
                     'tz' : '7200'
                   },
           'fj' : {
                     'country' : 'Fiji Islands',
                     'lat' : '-18.0000',
                     'continent' : 'Oceania',
                     'lon' : '175.0000',
                     'tz' : '43200'
                   },
           'ir' : {
                     'country' : 'Iran',
                     'lat' : '32.0000',
                     'continent' : 'Asia',
                     'lon' : '53.0000',
                     'tz' : '12600'
                   },
           'py' : {
                     'country' : 'Paraguay',
                     'lat' : '-23.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-58.0000',
                     'tz' : '-14400'
                   },
           'li' : {
                     'country' : 'Liechtenstein',
                     'lat' : '47.2667',
                     'continent' : 'Europe',
                     'lon' : '9.5333',
                     'tz' : '3600'
                   },
           'sn' : {
                     'country' : 'Senegal',
                     'lat' : '14.0000',
                     'continent' : 'Africa',
                     'lon' : '-14.0000',
                     'tz' : '0'
                   },
           'td' : {
                     'country' : 'Chad',
                     'lat' : '15.0000',
                     'continent' : 'Africa',
                     'lon' : '19.0000',
                     'tz' : '3600'
                   },
           'tz' : {
                     'country' : 'Tanzania',
                     'lat' : '-6.0000',
                     'continent' : 'Africa',
                     'lon' : '35.0000',
                     'tz' : '10800'
                   },
           'sd' : {
                     'country' : 'Sudan',
                     'lat' : '15.0000',
                     'continent' : 'Africa',
                     'lon' : '30.0000',
                     'tz' : '7200'
                   },
           'cg' : {
                     'country' : 'Democratic Republic of Congo (Zaire)',
                     'lat' : '-0.66207',
                     'continent' : 'Africa',
                     'lon' : '14.92742',
                     'tz' : '3600'
                   },
           'pa' : {
                     'country' : 'Panama',
                     'lat' : '9.0000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-80.0000',
                     'tz' : '-18000'
                   },
           'au' : {
                     'country' : 'Australia',
                     'lat' : '-27.0000',
                     'continent' : 'Oceania',
                     'lon' : '133.0000',
                     'tz' : '14400 '
                   },
           'sl' : {
                     'country' : 'Sierra Leone',
                     'lat' : '8.5000',
                     'continent' : 'Africa',
                     'lon' : '-11.5000',
                     'tz' : '0'
                   },
           'am' : {
                     'country' : 'Armenia',
                     'lat' : '40.0000',
                     'continent' : 'Europe',
                     'lon' : '45.0000',
                     'tz' : '14400'
                   },
           'us' : {
                     'country' : 'United States (-5 to -11 of GMT)',
                     'lat' : '38.15217',
                     'continent' : 'NorthAmerica',
                     'lon' : '-100.25006',
                     'tz' : '-28800'
                   },
           'gh' : {
                     'country' : 'Ghana',
                     'lat' : '8.0000',
                     'continent' : 'Africa',
                     'lon' : '-2.0000',
                     'tz' : '0'
                   },
           'tv' : {
                     'country' : 'Tuvalu',
                     'lat' : '-8.0000',
                     'continent' : 'Oceania',
                     'lon' : '178.0000',
                     'tz' : '43200'
                   },
           'jo' : {
                     'country' : 'Jordan',
                     'lat' : '31.0000',
                     'continent' : 'Asia',
                     'lon' : '36.0000',
                     'tz' : '7200'
                   },
           'bi' : {
                     'country' : 'Burundi',
                     'lat' : '-3.5000',
                     'continent' : 'Africa',
                     'lon' : '30.0000',
                     'tz' : '7200'
                   },
           'ee' : {
                     'country' : 'Estonia',
                     'lat' : '59.0000',
                     'continent' : 'Europe',
                     'lon' : '26.0000',
                     'tz' : '10800'
                   },
           'dz' : {
                     'country' : 'Algeria',
                     'lat' : '28.0000',
                     'continent' : 'Africa',
                     'lon' : '3.0000',
                     'tz' : '0'
                   },
           'pk' : {
                     'country' : 'Pakistan',
                     'lat' : '30.0000',
                     'continent' : 'Asia',
                     'lon' : '70.0000',
                     'tz' : '18000'
                   },
           'ye' : {
                     'country' : 'Yemen Arab Republic',
                     'lat' : '15.0000',
                     'continent' : 'Asia',
                     'lon' : '48.0000',
                     'tz' : '10800'
                   },
           'cm' : {
                     'country' : 'Cameroon',
                     'lat' : '6.0000',
                     'continent' : 'Africa',
                     'lon' : '12.0000',
                     'tz' : '3600'
                   },
           'bw' : {
                     'country' : 'Botswana',
                     'lat' : '-22.0000',
                     'continent' : 'Africa',
                     'lon' : '24.0000',
                     'tz' : '7200'
                   },
           'mn' : {
                     'country' : 'Mongolia',
                     'lat' : '46.0000',
                     'continent' : 'Asia',
                     'lon' : '105.0000',
                     'tz' : '28800'
                   },
           'gd' : {
                     'country' : 'Grenada',
                     'lat' : '12.1167',
                     'continent' : 'NorthAmerica',
                     'lon' : '-61.6667',
                     'tz' : '-14400'
                   },
           'lk' : {
                     'country' : 'Sri Lanka',
                     'lat' : '7.0000',
                     'continent' : 'Asia',
                     'lon' : '81.0000',
                     'tz' : '19800'
                   },
           'nz' : {
                     'country' : 'New Zealand',
                     'lat' : '-41.0000',
                     'continent' : 'Oceania',
                     'lon' : '174.0000',
                     'tz' : '43200'
                   },
           'ae' : {
                     'country' : 'United Arab Emirates',
                     'lat' : '24.0000',
                     'continent' : 'Asia',
                     'lon' : '54.0000',
                     'tz' : '14400'
                   },
           'mg' : {
                     'country' : 'Madagascar',
                     'lat' : '-20.0000',
                     'continent' : 'Africa',
                     'lon' : '47.0000',
                     'tz' : '10800'
                   },
           'sc' : {
                     'country' : 'Seychelles',
                     'lat' : '-4.5833',
                     'continent' : 'Africa',
                     'lon' : '55.6667',
                     'tz' : '14400'
                   },
           'cn' : {
                     'country' : 'China',
                     'lat' : '35.0000',
                     'continent' : 'Asia',
                     'lon' : '105.0000',
                     'tz' : '28800'
                   },
           'ru' : {
                     'country' : 'Russia',
                     'lat' : '60.0000',
                     'continent' : 'Asia',
                     'lon' : '100.0000',
                     'tz' : '10800'
                   },
           'ag' : {
                     'country' : 'Antigua and Barbuda',
                     'lat' : '17.0500',
                     'continent' : 'NorthAmerica',
                     'lon' : '-61.8000',
                     'tz' : '-14400'
                   },
           'mx' : {
                     'country' : 'Mexico',
                     'lat' : '23.0000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-102.0000',
                     'tz' : '-25200'
                   },
           'sy' : {
                     'country' : 'Syria',
                     'lat' : '35.0000',
                     'continent' : 'Asia',
                     'lon' : '38.0000',
                     'tz' : '7200'
                   },
           'cr' : {
                     'country' : 'Costa Rica',
                     'lat' : '10.0000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-84.0000',
                     'tz' : '-21600'
                   },
           'az' : {
                     'country' : 'Azerbaijan',
                     'lat' : '40.5000',
                     'continent' : 'Europe',
                     'lon' : '47.5000',
                     'tz' : '14400'
                   },
           'sg' : {
                     'country' : 'Singapore',
                     'lat' : '1.3667',
                     'continent' : 'Asia',
                     'lon' : '103.8000',
                     'tz' : '28800'
                   },
           'ec' : {
                     'country' : 'Ecuador',
                     'lat' : '-2.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-77.5000',
                     'tz' : '-18000'
                   },
           'mz' : {
                     'country' : 'Mozambique',
                     'lat' : '-18.2500',
                     'continent' : 'Africa',
                     'lon' : '35.0000',
                     'tz' : '7200'
                   },
           'bm' : {
                     'country' : 'Bermuda',
                     'lat' : '32.3333',
                     'continent' : 'NorthAmerica',
                     'lon' : '-64.7500',
                     'tz' : '-14400'
                   },
           'kh' : {
                     'country' : 'Cambodia',
                     'lat' : '13.0000',
                     'continent' : 'Asia',
                     'lon' : '105.0000',
                     'tz' : '25200'
                   },
           'lb' : {
                     'country' : 'Lebanon',
                     'lat' : '33.8333',
                     'continent' : 'Asia',
                     'lon' : '35.8333',
                     'tz' : '7200'
                   },
           'nr' : {
                     'country' : 'Nauru',
                     'lat' : '-0.5333',
                     'continent' : 'Oceania',
                     'lon' : '166.9167',
                     'tz' : '43200'
                   },
           'bz' : {
                     'country' : 'Belize',
                     'lat' : '17.2500',
                     'continent' : 'NorthAmerica',
                     'lon' : '-88.7500',
                     'tz' : '-21600'
                   },
           'vu' : {
                     'country' : 'Vanuatu',
                     'lat' : '-16.0000',
                     'continent' : 'Oceania',
                     'lon' : '167.0000',
                     'tz' : '39600'
                   },
           'kw' : {
                     'country' : 'Kuwait',
                     'lat' : '29.5000',
                     'continent' : 'Asia',
                     'lon' : '45.7500',
                     'tz' : '10800'
                   },
           'gf' : {
                     'country' : 'French Guiana',
                     'lat' : '4.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-53.0000',
                     'tz' : '-14400'
                   },
           'bj' : {
                     'country' : 'Benin',
                     'lat' : '9.5000',
                     'continent' : 'Africa',
                     'lon' : '2.2500',
                     'tz' : '3600'
                   },
           'al' : {
                     'country' : 'Albania',
                     'lat' : '41.0000',
                     'continent' : 'Europe',
                     'lon' : '20.0000',
                     'tz' : '3600'
                   },
           'uz' : {
                     'country' : 'Uzbekistan',
                     'lat' : '41.0000',
                     'continent' : 'Asia',
                     'lon' : '64.0000',
                     'tz' : '21600'
                   },
           'pr' : {
                     'country' : 'Puerto Rico',
                     'lat' : '18.2500',
                     'continent' : 'NorthAmerica',
                     'lon' : '-66.5000',
                     'tz' : '-14400'
                   },
           'lr' : {
                     'country' : 'Liberia',
                     'lat' : '6.5000',
                     'continent' : 'Africa',
                     'lon' : '-9.5000',
                     'tz' : '0'
                   },
           'fk' : {
                     'country' : 'Falkland Islands',
                     'lat' : '-51.9578',
                     'continent' : 'SouthAmerica',
                     'lon' : '-59.5288',
                     'tz' : '-14400'
                   },
           'nf' : {
                     'country' : 'Norfolk Island',
                     'lat' : '-29.0333',
                     'continent' : 'Oceania',
                     'lon' : '167.9500',
                     'tz' : '41400'
                   },
           'np' : {
                     'country' : 'Nepal',
                     'lat' : '28.0000',
                     'continent' : 'Asia',
                     'lon' : '84.0000',
                     'tz' : '19800'
                   },
           'ht' : {
                     'country' : 'Haiti',
                     'lat' : '19.0000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-72.4167',
                     'tz' : '-18000'
                   },
           'do' : {
                     'country' : 'Dominican Republic',
                     'lat' : '19.0000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-70.6667',
                     'tz' : '-14400'
                   },
           'mp' : {
                     'country' : 'Mariana Islands',
                     'lat' : '15.2',
                     'continent' : 'Oceania',
                     'lon' : '145.75',
                     'tz' : '3600'
                   },
           'bs' : {
                     'country' : 'Bahamas',
                     'lat' : '24.6949',
                     'continent' : 'NorthAmerica',
                     'lon' : '-77.4616',
                     'tz' : '-18000'
                   },
           'gm' : {
                     'country' : 'The Gambia',
                     'lat' : '13.4454',
                     'continent' : 'Africa',
                     'lon' : '-15.3114',
                     'tz' : '0'
                   },
           'mw' : {
                     'country' : 'Malawi',
                     'lat' : '-13.5000',
                     'continent' : 'Africa',
                     'lon' : '34.0000',
                     'tz' : '7200'
                   },
           'to' : {
                     'country' : 'Tonga',
                     'lat' : '-20.0000',
                     'continent' : 'Oceania',
                     'lon' : '-175.0000',
                     'tz' : '46800'
                   },
           'cu' : {
                     'country' : 'Cuba',
                     'lat' : '21.5000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-80.0000',
                     'tz' : '-10800'
                   },
           'ch' : {
                     'country' : 'Switzerland',
                     'lat' : '47.0000',
                     'continent' : 'Europe',
                     'lon' : '8.0000',
                     'tz' : '3600'
                   },
           'country2cc' : {
                             'Tuvalu' : 'tv',
                             'Sweden' : 'se',
                             'Tonga' : 'to',
                             'Nepal' : 'np',
                             'Anguilla' : 'ai',
                             'Somalia' : 'so',
                             'Nauru' : 'nr',
                             'Guyana' : 'gy',
                             'Mozambique' : 'mz',
                             'Samoa (Western)' : 'ws',
                             'Ethiopia' : 'et',
                             'Equatorial Guinea' : 'gq',
                             'South Africa' : 'za',
                             'Peru' : 'pe',
                             'Indonesia' : 'id',
                             'Argentina' : 'ar',
                             'Surinam' : 'sr',
                             'Portugal' : 'pt',
                             'Cook Islands' : 'ck',
                             'Nigeria' : 'ng',
                             'Solomon Islands' : 'sb',
                             'Mayotte Islands' : 'yt',
                             'Dominican Republic' : 'do',
                             'Antigua and Barbuda' : 'ag',
                             'Turkey' : 'tr',
                             'Micronesia' : 'fm',
                             'latvia' : 'lv',
                             'Morocco' : 'ma',
                             'Tunisia' : 'tn',
                             'Malawi' : 'mw',
                             'Cayman Islands' : 'ky',
                             'Mauritius' : 'mu',
                             'Mariana Islands' : 'mp',
                             'Bangladesh' : 'bd',
                             'Netherlands' : 'nl',
                             'Brazil' : 'br',
                             'Japan' : 'jp',
                             'Paraguay' : 'py',
                             'Ecuador' : 'ec',
                             'Croatia' : 'hr',
                             'Swaziland' : 'sz',
                             'Jamaica' : 'jm',
                             'Slovenia' : 'si',
                             'Israel' : 'il',
                             'Belize' : 'bz',
                             'Madagascar' : 'mg',
                             'Botswana' : 'bw',
                             'India' : 'io',
                             'Namibia' : 'na',
                             'Algeria' : 'dz',
                             'Malta' : 'mt',
                             'The Gambia' : 'gm',
                             'Columbia' : 'co',
                             'UK' : 'gb',
                             'Taiwan' : 'tw',
                             'Trinidad & Tobago' : 'tt',
                             'Falkland Islands' : 'fk',
                             'Bulgaria' : 'bg',
                             'Azerbaijan' : 'az',
                             'Macau' : 'mo',
                             'Laos' : 'la',
                             'Lebanon' : 'lb',
                             'Iraq' : 'iq',
                             'Thailand' : 'th',
                             'Barbados' : 'bb',
                             'United States (-5 to -11 of GMT)' : 'us',
                             'United Arab Emirates' : 'ae',
                             'Singapore' : 'sg',
                             'Belarus' : 'by',
                             'Bosnia' : 'ba',
                             'Vietnam' : 'vn',
                             'Ukraine' : 'ua',
                             'Maldives Republic' : 'mv',
                             'Romania' : 'ro',
                             'Cameroon' : 'cm',
                             'Greece' : 'gr',
                             'Grenada' : 'gd',
                             'Germany' : 'de',
                             'San Marino' : 'sm',
                             'Belgium' : 'be',
                             'Burkina Faso' : 'bf',
                             'Monaco' : 'mc',
                             'Chile' : 'cl',
                             'French Guiana' : 'gf',
                             'Uzbekistan' : 'uz',
                             'Slovak Republic' : 'sk',
                             'Wallis & Futuna Islands' : 'wf',
                             'Haiti' : 'ht',
                             'Costa Rica' : 'cr',
                             'France' : 'fr',
                             'Macedonia (Fyrom)' : 'mk',
                             'Korea 85' : 'kp',
                             'Kiribati' : 'ki',
                             'Malaysia' : 'my',
                             'Guam' : 'gu',
                             'Cambodia' : 'kh',
                             'Libya' : 'ly',
                             'Panama' : 'pa',
                             'Rwanda' : 'rw',
                             'Benin' : 'bj',
                             'Uruguay' : 'uy',
                             'Syria' : 'sy',
                             'Puerto Rico' : 'pr',
                             'Netherlands Antilles' : 'an',
                             'Mongolia' : 'mn',
                             'Hungary' : 'hu',
                             'Zambia' : 'zm',
                             'Liechtenstein' : 'li',
                             'Hong Kong' : 'hk',
                             'Pakistan' : 'pk',
                             'Central Africa Republic' : 'cf',
                             'Sri Lanka' : 'lk',
                             'China' : 'cn',
                             'Gibraltar' : 'gi',
                             'Sierra Leone' : 'sl',
                             'Estonia' : 'ee',
                             'Eritrea' : 'er',
                             'Angola' : 'ao',
                             'Guatemala' : 'gt',
                             'Democratic Republic of Congo (Zaire)' : 'cg',
                             'Armenia' : 'am',
                             'Saudi Arabia' : 'sa',
                             'Oman' : 'om',
                             'Turkmenistan' : 'tm',
                             'Honduras' : 'hn',
                             'Guadeloupe' : 'gp',
                             'Ireland' : 'ie',
                             'Vanuatu' : 'vu',
                             'Qatar' : 'qa',
                             'Nicaragua' : 'ni',
                             'Sao Tome & Principe' : 'st',
                             'Czech Republic' : 'cz',
                             'Myanmar (Burma)' : 'mm',
                             'Iceland' : 'is',
                             'Fiji Islands' : 'fj',
                             'Ghana' : 'gh',
                             'French Polynesia' : 'pf',
                             'Mexico' : 'mx',
                             'Bahamas' : 'bs',
                             'Djibouti' : 'dj',
                             'Guinea Bissau' : 'gw',
                             'El Salvador' : 'sv',
                             'Tajikistan' : 'tj',
                             'Poland' : 'pl',
                             'Aruba' : 'aw',
                             'Turks & Caicos Islands' : 'tc',
                             'Togo' : 'tg',
                             'Guinea Republic' : 'gn',
                             'Ivory Coast' : 'ci',
                             'Cuba' : 'cu',
                             'Moldova' : 'md',
                             'Yemen Arab Republic' : 'ye',
                             'Spain' : 'es',
                             'Comoros Island' : 'km',
                             'Kenya' : 'ke',
                             'Gabon' : 'ga',
                             'Bolivia' : 'bo',
                             'Egypt' : 'eg',
                             'Australia' : 'au',
                             'Switzerland' : 'ch',
                             'Lithuania' : 'lt',
                             'Montserrat' : 'ms',
                             'Marshall Islands' : 'mh',
                             'Norway' : 'no',
                             'Canada' : 'ca',
                             'Cyprus' : 'cy',
                             'Luxembourg' : 'lu',
                             'Papua New Guinea' : 'pg',
                             'Brunei' : 'bn',
                             'Reunion Island' : 're',
                             'Bermuda' : 'bm',
                             'Iran' : 'ir',
                             'Korea 82' : 'kr',
                             'Kyrgyzstan' : 'kg',
                             'Martinique' : 'mq',
                             'Seychelles' : 'sc',
                             'Russia' : 'ru',
                             'Finland' : 'fi',
                             'Tanzania' : 'tz',
                             'Palau' : 'pw',
                             'Chad' : 'td',
                             'Austria' : 'at',
                             'Kazakhstan' : 'kz',
                             'Lesotho' : 'ls',
                             'Jordan' : 'jo',
                             'Italy' : 'it',
                             'Uganda' : 'ug',
                             'Philippines' : 'ph',
                             'Zimbabwe' : 'zw',
                             'Bhutan' : 'bt',
                             'New Zealand' : 'nz',
                             'Liberia' : 'lr',
                             'Bahrain' : 'bh',
                             'Burundi' : 'bi',
                             'Faeroe Islands' : 'fo',
                             'Kuwait' : 'kw',
                             'Cape Verde Islands' : 'cv',
                             'Venezuela' : 've',
                             'Niue Island' : 'nu',
                             'Georgia' : 'ge',
                             'New Caledonia' : 'nc',
                             'Sudan' : 'sd',
                             'Greenland' : 'gl',
                             'Denmark' : 'dk',
                             'Andorra' : 'ad',
                             'Senegal' : 'sn',
                             'Norfolk Island' : 'nf',
                             'Albania' : 'al'
                           },
           'mu' : {
                     'country' : 'Mauritius',
                     'lat' : '-20.2833',
                     'continent' : 'Africa',
                     'lon' : '57.5500',
                     'tz' : '14400'
                   },
           'ni' : {
                     'country' : 'Nicaragua',
                     'lat' : '13.0000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-85.0000',
                     'tz' : '-21600'
                   },
           'gu' : {
                     'country' : 'Guam',
                     'lat' : '13.4667',
                     'continent' : 'NorthAmerica',
                     'lon' : '144.7833',
                     'tz' : '3600'
                   },
           'bg' : {
                     'country' : 'Bulgaria',
                     'lat' : '43.0000',
                     'continent' : 'Europe',
                     'lon' : '25.0000',
                     'tz' : '7200'
                   },
           'pw' : {
                     'country' : 'Palau',
                     'lat' : '7.5000',
                     'continent' : 'Oceania',
                     'lon' : '134.5000',
                     'tz' : '32400'
                   },
           'aw' : {
                     'country' : 'Aruba',
                     'lat' : '12.5000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-69.9667',
                     'tz' : '-14400'
                   },
           'gy' : {
                     'country' : 'Guyana',
                     'lat' : '5.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-59.0000',
                     'tz' : '-10800'
                   },
           'ca' : {
                     'country' : 'Canada',
                     'lat' : '60.0000',
                     'continent' : 'NorthAmerica',
                     'lon' : '-95.0000',
                     'tz' : '-28800'
                   },
           'pl' : {
                     'country' : 'Poland',
                     'lat' : '52.0000',
                     'continent' : 'Europe',
                     'lon' : '20.0000',
                     'tz' : '3600'
                   },
           'sk' : {
                     'country' : 'Slovak Republic',
                     'lat' : '46.1167',
                     'continent' : 'Europe',
                     'lon' : '14.8167',
                     'tz' : '3600'
                   },
           'pe' : {
                     'country' : 'Peru',
                     'lat' : '-10.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-76.0000',
                     'tz' : '-18000'
                   },
           'an' : {
                     'country' : 'Netherlands Antilles',
                     'lat' : '12.2500',
                     'continent' : 'Oceania',
                     'lon' : '-68.7500',
                     'tz' : '-14400'
                   },
           'ua' : {
                     'country' : 'Ukraine',
                     'lat' : '49.0000',
                     'continent' : 'Europe',
                     'lon' : '32.0000',
                     'tz' : '10800'
                   },
           'uk' : {
   	              'country' : 'UK',
   	              'lat' : '55.40342',
   	              'continent' : 'Europe',
   	              'lon' : '-3.21145',
   	              'tz' : '0'
   	            },
           'gw' : {
                     'country' : 'Guinea Bissau',
                     'lat' : '11.0000',
                     'continent' : 'Africa',
                     'lon' : '-10.0000',
                     'tz' : '-3600'
                   },
           'es' : {
                     'country' : 'Spain',
                     'lat' : '40.0000',
                     'continent' : 'Europe',
                     'lon' : '-4.0000',
                     'tz' : '3600'
                   },
           'kr' : {
                     'country' : 'Korea 82',
                     'lat' : '36.0575',
                     'continent' : 'Asia',
                     'lon' : '127.3356',
                     'tz' : '32400'
                   },
           'tt' : {
                     'country' : 'Trinidad & Tobago',
                     'lat' : '11',
                     'continent' : 'NorthAmerica',
                     'lon' : '-61',
                     'tz' : '-14400'
                   },
           'ca -21600 -14400' : {
                                   'country' : 'Canada',
                                   'tz' : '-28800'
                                 },
           'fo' : {
                     'country' : 'Faeroe Islands',
                     'lat' : 'NaN',
                     'continent' : 'Oceania',
                     'lon' : 'NaN',
                     'tz' : '+0'
                   },
           'yt' : {
                     'country' : 'Mayotte Islands',
                     'lat' : '-12.8333',
                     'continent' : 'Oceania',
                     'lon' : '45.1667',
                     'tz' : '10800'
                   },
           'kp' : {
                     'country' : 'Korea 85',
                     'lat' : '36.0575',
                     'continent' : 'Asia',
                     'lon' : '127.3356',
                     'tz' : '32400'
                   },
           'bb' : {
                     'country' : 'Barbados',
                     'lat' : '13.1667',
                     'continent' : 'NorthAmerica',
                     'lon' : '-59.5333',
                     'tz' : '-14400'
                   },
           'sa' : {
                     'country' : 'Saudi Arabia',
                     'lat' : '25.0000',
                     'continent' : 'Asia',
                     'lon' : '45.0000',
                     'tz' : '10800'
                   },
           'io' : {
                     'country' : 'India',
                     'lat' : '20.0000',
                     'continent' : 'Oceania',
                     'lon' : '77.0000',
                     'tz' : '18000.5'
                   },
           'zm' : {
                     'country' : 'Zambia',
                     'lat' : '-15.0000',
                     'continent' : 'Africa',
                     'lon' : '30.0000',
                     'tz' : '7200'
                   },
           'hk' : {
                     'country' : 'Hong Kong',
                     'lat' : '22.2500',
                     'continent' : 'Asia',
                     'lon' : '114.1667',
                     'tz' : '28800'
                   },
           'th' : {
                     'country' : 'Thailand',
                     'lat' : '15.0000',
                     'continent' : 'Asia',
                     'lon' : '100.0000',
                     'tz' : '25200'
                   },
           'ie' : {
                     'country' : 'Ireland',
                     'lat' : '53.0000',
                     'continent' : 'Europe',
                     'lon' : '-8.0000',
                     'tz' : '0'
                   },
           'et' : {
                     'country' : 'Ethiopia',
                     'lat' : '8.0000',
                     'continent' : 'Africa',
                     'lon' : '38.0000',
                     'tz' : '10800'
                   },
           'so' : {
                     'country' : 'Somalia',
                     'lat' : '10.0000',
                     'continent' : 'Africa',
                     'lon' : '49.0000',
                     'tz' : '10800'
                   },
           'er' : {
                     'country' : 'Eritrea',
                     'lat' : '15.0000',
                     'continent' : 'Africa',
                     'lon' : '39.0000',
                     'tz' : '10800'
                   },
           'cf' : {
                     'country' : 'Central Africa Republic',
                     'lat' : '7.0000',
                     'continent' : 'Africa',
                     'lon' : '21.0000',
                     'tz' : '3600'
                   },
           'tj' : {
                     'country' : 'Tajikistan',
                     'lat' : '39.0000',
                     'continent' : 'Asia',
                     'lon' : '71.0000',
                     'tz' : '21600'
                   },
           'cz' : {
                     'country' : 'Czech Republic',
                     'lat' : '49.7500',
                     'continent' : 'Europe',
                     'lon' : '15.5000',
                     'tz' : '3600'
                   },
           'mk' : {
                     'country' : 'Macedonia (Fyrom)',
                     'lat' : '41.8333',
                     'continent' : 'Europe',
                     'lon' : '22.0000',
                     'tz' : '3600'
                   },
           'lt' : {
                     'country' : 'Lithuania',
                     'lat' : '56.0000',
                     'continent' : 'Europe',
                     'lon' : '24.0000',
                     'tz' : '7200'
                   },
           'hr' : {
                     'country' : 'Croatia',
                     'lat' : '45.1667',
                     'continent' : 'Europe',
                     'lon' : '15.5000',
                     'tz' : '3600'
                   },
           'gn' : {
                     'country' : 'Guinea Republic',
                     'lat' : '11.0000',
                     'continent' : 'Africa',
                     'lon' : '-10.0000',
                     'tz' : '0'
                   },
           'de' : {
                     'country' : 'Germany',
                     'lat' : '51.0000',
                     'continent' : 'Europe',
                     'lon' : '9.0000',
                     'tz' : '3600'
                   },
           'be' : {
                     'country' : 'Belgium',
                     'lat' : '50.8333',
                     'continent' : 'Europe',
                     'lon' : '4.0000',
                     'tz' : '3600'
                   },
           'qa' : {
                     'country' : 'Qatar',
                     'lat' : '25.5000',
                     'continent' : 'Asia',
                     'lon' : '51.2500',
                     'tz' : '10800'
                   },
           'cv' : {
                     'country' : 'Cape Verde Islands',
                     'lat' : '16.0000',
                     'continent' : 'Africa',
                     'lon' : '-24.0000',
                     'tz' : '-3600'
                   },
           'md' : {
                     'country' : 'Moldova',
                     'lat' : '47.0000',
                     'continent' : 'Europe',
                     'lon' : '29.0000',
                     'tz' : '10800'
                   },
           'fm' : {
                     'country' : 'Micronesia',
                     'lat' : '8.4674',
                     'continent' : 'Oceania',
                     'lon' : '150.5438',
                     'tz' : '3600'
                   },
           'jp' : {
                     'country' : 'Japan',
                     'lat' : '36.0000',
                     'continent' : 'Asia',
                     'lon' : '138.0000',
                     'tz' : '32400'
                   },
           'cl' : {
                     'country' : 'Chile',
                     'lat' : '-30.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-71.0000',
                     'tz' : '-14400'
                   },
           'tw' : {
                     'country' : 'Taiwan',
                     'lat' : '23.5000',
                     'continent' : 'Asia',
                     'lon' : '121.0000',
                     'tz' : '28800'
                   },
           'ws' : {
                     'country' : 'Samoa (Western)',
                     'lat' : '-13.5833',
                     'continent' : 'Oceania',
                     'lon' : '-172.3333',
                     'tz' : '-39600'
                   },
           'ad' : {
                     'country' : 'Andorra',
                     'lat' : '42.5000',
                     'continent' : 'Europe',
                     'lon' : '1.5000',
                     'tz' : '3600'
                   },
           'sz' : {
                     'country' : 'Swaziland',
                     'lat' : '-26.5000',
                     'continent' : 'Africa',
                     'lon' : '31.5000',
                     'tz' : '7200'
                   },
           'bn' : {
                     'country' : 'Brunei',
                     'lat' : '4.5000',
                     'continent' : 'Asia',
                     'lon' : '114.6667',
                     'tz' : '28800'
                   },
           'at' : {
                     'country' : 'Austria',
                     'lat' : '47.3333',
                     'continent' : 'Europe',
                     'lon' : '13.3333',
                     'tz' : '3600'
                   },
           'tg' : {
                     'country' : 'Togo',
                     'lat' : '8.0000',
                     'continent' : 'Africa',
                     'lon' : '1.1667',
                     'tz' : '0'
                   },
           'vn' : {
                     'country' : 'Vietnam',
                     'lat' : '16.0000',
                     'continent' : 'Asia',
                     'lon' : '106.0000',
                     'tz' : '25200'
                   },
           'zw' : {
                     'country' : 'Zimbabwe',
                     'lat' : '-20.0000',
                     'continent' : 'Africa',
                     'lon' : '30.0000',
                     'tz' : '7200'
                   },
           'gp' : {
                     'country' : 'Guadeloupe',
                     'lat' : '16.2500',
                     'continent' : 'SouthAmerica',
                     'lon' : '-61.5833',
                     'tz' : '-14400'
                   },
           'ar' : {
                     'country' : 'Argentina',
                     'lat' : '-34.0000',
                     'continent' : 'SouthAmerica',
                     'lon' : '-64.0000',
                     'tz' : '-10800'
                   },
           'nl' : {
                     'country' : 'Netherlands',
                     'lat' : '52.5000',
                     'continent' : 'Europe',
                     'lon' : '5.7500',
                     'tz' : '3600'
                   },
           'sm' : {
                     'country' : 'San Marino',
                     'lat' : '43.7667',
                     'continent' : 'Europe',
                     'lon' : '12.4167',
                     'tz' : '3600'
                   },
           'dj' : {
                     'country' : 'Djibouti',
                     'lat' : '11.5000',
                     'continent' : 'Africa',
                     'lon' : '43.0000',
                     'tz' : '10800'
                   },
		   'ax' : {
                     'country' : 'Aland Islands',
                     'lat' : '60.116667',
                     'continent' : 'Europe',
                     'lon' : '19.9',
                     'tz' : '7200'
				  }
         }
