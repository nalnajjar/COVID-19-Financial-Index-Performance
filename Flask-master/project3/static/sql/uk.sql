--Drop Tables--
drop table ftse_uk;
drop table covid_uk;

--Create Tables--
create table ftse_uk(
	time VARCHAR,
	open VARCHAR,
	high VARCHAR,
	low VARCHAR,
	last VARCHAR,
	change VARCHAR,
	volume VARCHAR,
	open_int VARCHAR);

create table covid_uk(
	daterep VARCHAR,
	day VARCHAR,
	month VARCHAR,
	year VARCHAR,
	cases INT,
	deaths INT,
	countries_and_territories VARCHAR,
	GeoId VARCHAR,
    countryterritorycode VARCHAR,
	popdata2018 INT);
	
--Check Data--
select * from ftse_uk;
select * from covid_uk;

--Drop Extra Column from ftse_uk--
alter table ftse_uk drop open_int;

--Combine on Date--
create view uk_combined as 
select ftse_uk.time,
		ftse_uk.open,
		ftse_uk.high,
		ftse_uk.low,
		ftse_uk.last,
		ftse_uk.change,
		ftse_uk.volume,
		covid_uk.cases,
		covid_uk.deaths,
		covid_uk.geoid
from ftse_uk
inner join covid_uk on
ftse_uk.time = covid_uk.daterep;

select * from uk_combined;