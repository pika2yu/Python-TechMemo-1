#
# parsearg を使って、以下を定義して使うサンプル
#  - 必須の引数
#  - オプションのフラグ
#  - オプションの入力
# 

import argparse 
    # argparse を import する。
    # Python のパッケージにあらかじめ入っているので pip でライブラリをつかする必要はない。

#----------------------------
# argparserのインスタンスを生成する。
#----------------------------
#   description=... でプログラムの説明を定義できる。
parser = argparse.ArgumentParser(description='parsearg の使い方のサンプル。')

#----------------------------
# パラメータを定義する。
#----------------------------
# 必須パラメータは - や -- をつけない。
# コードで定義されている順に、引数がパースされる。
# 必須なので指定されていないとエラー。--> argparse が 足りないパラメータを指定するようにメッセージを出してくれる。
parser.add_argument('userid', help='１番目の位置引数。- や --をつけないと、順番に従って、その名前の値が与えられるように処理される。')
parser.add_argument('password', help='２番目の位置引数')

#
# オプションのパラメータは -- をつけて定義する。
# 1文字の省略形を - で定義する事も可能。
# お勧めではないが ２文字以上のパラメータを - だけで定義することもできる。
parser.add_argument('--sample_flag', action='store_true', help='ON/OFFのフラグのサンプル。')
    # action を指定するとフラグになる。
    # ='store_true' とすると、パラメータがあると True, 無いと False のフラグになる。
    # ='store_false' とすると逆になる。
parser.add_argument('-v', '--sample_value', default='デフォルトの値です', help='値を入力するためのパラメータのサンプル')
    # actionをつけないと値を伴うオプション。
    # default でデフォルト値を指定する事も可能。指定しないとデフォルトは None になる。

parser.add_argument('-abc', action='store_true', help='-で２文字以上のパラメータを指定する時の例')
    # -が１つになっているだけで、他の書き方は -- の時と書き方は同じ
    # 上の例だと a b c の３つを指定した場合と区別がつきづらくなるので、好ましい使い方とされていない。

#----------------------------
# パラメータをパースする。
#   以後、 arg.XXX でパラメータにアクセスできる。
#----------------------------
args = parser.parse_args()

if args.sample_flag:
    print('sample_flag is ON')
else:
    print('sample_flag is OFF')

print(f'userid={args.userid}')
print(f'password={args.password}')

print(f'sample_value={args.sample_value}')

if args.abc:
    print('abc is ON')
else:
    print('abc is OFF')
