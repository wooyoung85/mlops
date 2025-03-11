from __future__ import annotations

import json
from datetime import datetime, timedelta

import pandas as pd
import pendulum
import requests

from airflow import DAG
from airflow.operators.python import PythonOperator


# 데이터 추출 함수
def extract_data(**kwargs):
    end_date = datetime.now()
    end_date_str = end_date.strftime("%Y%m%d")
    start_date = end_date - timedelta(days=1)
    start_date_str = start_date.strftime("%Y%m%d")

    res = requests.post(
        "https://ecos.bok.or.kr/serviceEndpoint/httpService/request.json",
        headers={
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://ecos.bok.or.kr",
            "Referer": "https://ecos.bok.or.kr/",
        },
        json={
            "header": {
                "guidSeq": 1,
                "trxCd": "OSUUA02R01",
                "scrId": "IECOSPCM02",
                "sysCd": "03",
                "fstChnCd": "WEB",
                "langDvsnCd": "KO",
                "envDvsnCd": "D",
                "sndRspnDvsnCd": "S",
                "sndDtm": "20250103",
                "ipAddr": "211.38.3.194",
                "usrId": "IECOSPC",
                "pageNum": 1,
                "pageCnt": 1000,
            },
            "data": {
                "statSrchDsList": [
                    {
                        "dsItmValNm1": "원/미국달러(매매기준율)",
                        "dsItmValEngNm1": "Won per United States Dollar(Basic Exchange Rate)",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000001",
                    },
                    {
                        "dsItmValNm1": "원/위안(매매기준율)",
                        "dsItmValEngNm1": "Won per Yuan(Basic Exchange Rate)",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000053",
                    },
                    {
                        "dsItmValNm1": "원/일본엔(100엔)",
                        "dsItmValEngNm1": "Won per Japanese Yen(100Yen)",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000002",
                    },
                    {
                        "dsItmValNm1": "원/유로",
                        "dsItmValEngNm1": "Won per Euro",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000003",
                    },
                    {
                        "dsItmValNm1": "원/독일마르크",
                        "dsItmValEngNm1": "Won per German Mark",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000004",
                    },
                    {
                        "dsItmValNm1": "원/프랑스프랑",
                        "dsItmValEngNm1": "Won per French Franc",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000005",
                    },
                    {
                        "dsItmValNm1": "원/이태리리라(100리라)",
                        "dsItmValEngNm1": "Won per Italian Lira(100Lira)",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000006",
                    },
                    {
                        "dsItmValNm1": "원/벨기에프랑",
                        "dsItmValEngNm1": "Won per Belgian Franc",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000007",
                    },
                    {
                        "dsItmValNm1": "원/오스트리아실링",
                        "dsItmValEngNm1": "Won per Austrian Schilling",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000008",
                    },
                    {
                        "dsItmValNm1": "원/네덜란드길더",
                        "dsItmValEngNm1": "Won per Netherlands Guilder",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000009",
                    },
                    {
                        "dsItmValNm1": "원/스페인페세타(100페세타)",
                        "dsItmValEngNm1": "Won per Spanish Peseta(100Peseta)",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000010",
                    },
                    {
                        "dsItmValNm1": "원/핀란드마르카",
                        "dsItmValEngNm1": "Won per Finland Markka",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000011",
                    },
                    {
                        "dsItmValNm1": "원/영국파운드",
                        "dsItmValEngNm1": "Won per United Kingdom Pound",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000012",
                    },
                    {
                        "dsItmValNm1": "원/캐나다달러",
                        "dsItmValEngNm1": "Won per Canadian Dollar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000013",
                    },
                    {
                        "dsItmValNm1": "원/스위스프랑",
                        "dsItmValEngNm1": "Won per Swiss Franc",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000014",
                    },
                    {
                        "dsItmValNm1": "원/호주달러",
                        "dsItmValEngNm1": "Won per Australian Dollar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000017",
                    },
                    {
                        "dsItmValNm1": "원/뉴질랜드달러",
                        "dsItmValEngNm1": "Won per New Zealand Dollar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000026",
                    },
                    {
                        "dsItmValNm1": "원/중국위안",
                        "dsItmValEngNm1": "Won per Chinese Renminbi(China Yuan)",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000027",
                    },
                    {
                        "dsItmValNm1": "원/홍콩위안",
                        "dsItmValEngNm1": "Won per Chinese Renminbi(Hong Kong Yuan)",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000030",
                    },
                    {
                        "dsItmValNm1": "원/홍콩달러",
                        "dsItmValEngNm1": "Won per Hongkong Dollar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000015",
                    },
                    {
                        "dsItmValNm1": "원/대만달러",
                        "dsItmValEngNm1": "Won per Taiwanese Dollar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000031",
                    },
                    {
                        "dsItmValNm1": "원/몽골투그릭",
                        "dsItmValEngNm1": "Won per Mongolian Tugrik",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000032",
                    },
                    {
                        "dsItmValNm1": "원/카자흐스탄텡게",
                        "dsItmValEngNm1": "Won per Kazakhstan Tenge",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000033",
                    },
                    {
                        "dsItmValNm1": "원/태국바트",
                        "dsItmValEngNm1": "Won per Thai Baht",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000028",
                    },
                    {
                        "dsItmValNm1": "원/싱가포르달러",
                        "dsItmValEngNm1": "Won per Singapore Dollar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000024",
                    },
                    {
                        "dsItmValNm1": "원/인도네시아루피아(100루피아)",
                        "dsItmValEngNm1": "Won per Indonesian Rupiah",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000029",
                    },
                    {
                        "dsItmValNm1": "원/말레이지아링깃",
                        "dsItmValEngNm1": "Won per Malaysian Ringgit",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000025",
                    },
                    {
                        "dsItmValNm1": "원/필리핀페소",
                        "dsItmValEngNm1": "Won per Philippine Peso",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000034",
                    },
                    {
                        "dsItmValNm1": "원/베트남동(100동)",
                        "dsItmValEngNm1": "Won per Vietnamese Dong",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000035",
                    },
                    {
                        "dsItmValNm1": "원/브루나이달러",
                        "dsItmValEngNm1": "Won per Brunei Dollar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000036",
                    },
                    {
                        "dsItmValNm1": "원/인도루피",
                        "dsItmValEngNm1": "Won per Indian Rupee",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000037",
                    },
                    {
                        "dsItmValNm1": "원/파키스탄루피",
                        "dsItmValEngNm1": "Won per Pakistani Rupee",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000038",
                    },
                    {
                        "dsItmValNm1": "원/방글라데시타카",
                        "dsItmValEngNm1": "Won per Bangladesh Taka",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000039",
                    },
                    {
                        "dsItmValNm1": "원/멕시코 페소",
                        "dsItmValEngNm1": "Won per Mexican Peso",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000040",
                    },
                    {
                        "dsItmValNm1": "원/브라질 헤알",
                        "dsItmValEngNm1": "Won per Brazilian Real",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000041",
                    },
                    {
                        "dsItmValNm1": "원/아르헨티나페소",
                        "dsItmValEngNm1": "Won per Argentine Peso",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000042",
                    },
                    {
                        "dsItmValNm1": "원/스웨덴크로나",
                        "dsItmValEngNm1": "Won per Swdish Krona",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000016",
                    },
                    {
                        "dsItmValNm1": "원/덴마크크로나",
                        "dsItmValEngNm1": "Won per Danish Krone",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000018",
                    },
                    {
                        "dsItmValNm1": "원/노르웨이크로나",
                        "dsItmValEngNm1": "Won per Norwagian Krone",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000019",
                    },
                    {
                        "dsItmValNm1": "원/러시아루블",
                        "dsItmValEngNm1": "Won per Russian Ruble",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000043",
                    },
                    {
                        "dsItmValNm1": "원/헝가리포린트",
                        "dsItmValEngNm1": "Won per Hungarian Forint",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000044",
                    },
                    {
                        "dsItmValNm1": "원/폴란트즈워티",
                        "dsItmValEngNm1": "Won per Polish Zloty",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000045",
                    },
                    {
                        "dsItmValNm1": "원/체코코루나",
                        "dsItmValEngNm1": "Won per Czech Koruna",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000046",
                    },
                    {
                        "dsItmValNm1": "원/사우디아라비아리얄",
                        "dsItmValEngNm1": "Won per Saudi Riyal",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000020",
                    },
                    {
                        "dsItmValNm1": "원/카타르리얄",
                        "dsItmValEngNm1": "Won per Qatari Riyal",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000047",
                    },
                    {
                        "dsItmValNm1": "원/이스라엘셰켈",
                        "dsItmValEngNm1": "Won per Israeli Shekel",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000048",
                    },
                    {
                        "dsItmValNm1": "원/요르단디나르",
                        "dsItmValEngNm1": "Won per Jordanian Dinar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000049",
                    },
                    {
                        "dsItmValNm1": "원/쿠웨이트디나르",
                        "dsItmValEngNm1": "Won per Kuwaiti Dinar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000021",
                    },
                    {
                        "dsItmValNm1": "원/바레인디나르",
                        "dsItmValEngNm1": "Won per Bahraini Dinar",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000022",
                    },
                    {
                        "dsItmValNm1": "원/아랍에미리트디르함",
                        "dsItmValEngNm1": "Won per United Arab Emirates Dirham",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000023",
                    },
                    {
                        "dsItmValNm1": "원/튀르키예리라",
                        "dsItmValEngNm1": "Won per Turkish Lira",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000050",
                    },
                    {
                        "dsItmValNm1": "원/남아프리카공화국랜드",
                        "dsItmValEngNm1": "Won per South African Rand",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000051",
                    },
                    {
                        "dsItmValNm1": "원/이집트파운드",
                        "dsItmValEngNm1": "Won per Egyptian Pound",
                        "dsId": "731Y001",
                        "dsItmId1": "ACC_ITEM",
                        "dsItmGrpId1": "G12023",
                        "dsItmVal1": "0000052",
                    },
                ],
                "statSrchFreqList": [
                    {
                        "freq": "D",
                        "vlidStDtm": start_date_str,
                        "vlidEndDtm": end_date_str,
                    }
                ],
                "statSrchFreqList": [
                    {
                        "freq": "D",
                        "vlidStDtm": start_date_str,
                        "vlidEndDtm": end_date_str,
                    }
                ],
                "statTyp": "E",
                "statDataCvsnCdList": ["00"],
                "viewType": "01",
                "holidayYn": "Y",
            },
        },
    )

    res_json = res.json()
    json_data = res_json["data"]["jsonCtnt"]
    return json.loads(json_data)


# 데이터 저장 함수
def save_to_csv(**kwargs):
    ti = kwargs['ti']
    json_data = ti.xcom_pull(task_ids='extract_data')

    df = pd.DataFrame(json_data)
    start_date = datetime.now() - timedelta(days=1)
    end_date = datetime.now()
    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = end_date.strftime("%Y%m%d")

    # 파일 경로 지정
    file_path = f"/opt/airflow/dags/df_{start_date_str}-{end_date_str}.csv"
    
    # CSV 파일 저장
    df.to_csv(file_path, index=False)


# DAG 정의
default_args = {
    'owner': 'airflow',
    'start_date': pendulum.datetime(2023, 1, 1, tz="UTC"),
    'retries': 2,
}

with DAG(
    'exchange_rate_dag',
    default_args=default_args,
    description='A DAG to fetch exchange rates and save to CSV',
    schedule_interval='@daily',
    catchup=False,
    tags=['example'],
) as dag:

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
        provide_context=True,
    )

    save_task = PythonOperator(
        task_id='save_to_csv',
        python_callable=save_to_csv,
        provide_context=True,
    )

    extract_task >> save_task
