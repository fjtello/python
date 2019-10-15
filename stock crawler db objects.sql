USE [STOCK]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Files](
	[idFile] [int] IDENTITY(1,1) NOT NULL,
	[CodFile] [varchar](20) NOT NULL,
	[Ticker] [varchar](20) NOT NULL,
	[Path] [varchar](255) NOT NULL,
	[URLSource] [varchar](255) NULL,
	[Enabled] [int] NULL,
	[DownloadLink] [varchar](255) NULL,
	[DownloadedFileName] [varchar](255) NULL,
	[Description] [varchar](100) NULL,
 CONSTRAINT [PK_Files] PRIMARY KEY CLUSTERED 
(
	[idFile] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[StockValues](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[ticker] [varchar](20) NULL,
	[Dt] [date] NULL,
	[Open] [decimal](10, 4) NULL,
	[High] [decimal](10, 4) NULL,
	[Low] [decimal](10, 4) NULL,
	[Close] [decimal](10, 4) NULL,
	[Adj Close] [decimal](10, 4) NULL,
	[Volume] [bigint] NULL,
	[Creation] [datetime] NOT NULL,
	[Updated] [datetime] NULL,
 CONSTRAINT [PK_StockValues] PRIMARY KEY CLUSTERED 
([id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[StockValues] ADD  CONSTRAINT [DF_StockValues_Creation]  DEFAULT (getdate()) FOR [Creation]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		fjtello
-- Create date: 2019.09.06
-- Description:	Lectura de la tabla de archivos
-- =============================================

CREATE PROCEDURE [dbo].[proc_Files_Select]
AS
BEGIN
	SET NOCOUNT ON;

	SELECT codFile, ticker, path, urlSource, downloadLink, DownloadedFileName 
	FROM FILES 
	WHERE ISNULL(enabled, 0) = 1 
	ORDER BY codFile
END
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- =============================================
-- Author:		fjtello
-- Create date: 2019.09.06
-- Description:	Inserción en la tabla de valores
-- =============================================
CREATE PROCEDURE [dbo].[proc_StockValues_Insert]
	@par_ticker VARCHAR(20), 
	@par_Dt DATE, 
	@par_Open DECIMAL(10, 4), 
	@par_High DECIMAL(10, 4), 
	@par_Low DECIMAL(10, 4),
	@par_Close DECIMAL(10, 4), 
	@par_AdjClose DECIMAL(10, 4), 
	@par_Volume BIGINT, 
	@replace INT = NULL
AS
BEGIN
	SET NOCOUNT ON;

	if ISNULL(@replace, 0) = 1
		begin
			
			if(select count(*) from [stockValues] where ticker = @par_ticker and dt = @par_Dt) > 0
				begin
					update [stockValues] 
						set 
						[Open] = @par_Open, 
						[High] = @par_High, 
						[Low] = @par_Low, 
						[Close] = @par_Close, 
						[Adj Close] = @par_AdjClose, 
						[Volume] = @par_Volume,
						[updated] = getdate()
					where ticker = @par_ticker and Dt = @par_Dt
				end
			else
				begin
					INSERT INTO [dbo].[stockValues]
						([ticker], [Dt], [Open], [High], [Low], [Close], [Adj Close], [Volume])
					VALUES
						(@par_ticker, @par_Dt, @par_Open, @par_High, @par_Low, @par_Close, @par_AdjClose, @par_Volume)
				end
		end
	else
		begin
			INSERT INTO [dbo].[stockValues]
				([ticker], [Dt], [Open], [High], [Low], [Close], [Adj Close], [Volume])
			VALUES
				(@par_ticker, @par_Dt, @par_Open, @par_High, @par_Low, @par_Close, @par_AdjClose, @par_Volume)
		end	
END
GO




INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('ACS', 'ACS', 'C:\BI Projects\YahooFinance\source\ACS.MC.csv', 'https://finance.yahoo.com/quote/ACS.MC/history?p=ACS.MC&.tsrc=fin-srch', 1, 'https://query1.finance.yahoo.com/v7/finance/download/ACS.MC?period1=[periodo_inicial]&dummy1=1537101465&period2=[periodo_final]&dummy2=1568637465&interval=1d&events=history&crumb=UogmSXpOr49', 'ACS.MC.csv', 'Grupo ACS');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('AENA', 'AENA', 'C:\BI Projects\YahooFinance\source\AENA.MC.csv', 'https://finance.yahoo.com/quote/AENA.MC/history?p=AENA.MC&.tsrc=fin-srch', 1, 'https://query1.finance.yahoo.com/v7/finance/download/AENA.MC?period1=[periodo_inicial]&dummy1=1537101465&period2=[periodo_final]&dummy2=1568637465&interval=1d&events=history&crumb=UogmSXpOr49', 'AENA.MC.csv', 'Aena');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('AMS', 'AMS', 'C:\BI Projects\YahooFinance\source\AMS.MC.csv', 'https://es.finance.yahoo.com/quote/AMS.MC/history?p=AMS.MC&.tsrc=fin-srch', 1, 'https://query1.finance.yahoo.com/v7/finance/download/AMS.MC?period1=[periodo_inicial]&dummy1=1537101084&period2=[periodo_final]&dummy2=1568637084&interval=1d&events=history&crumb=UogmSXpOr49', 'AMS.MC.csv', 'Amadeus IT Group');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('BBVA', 'BBVA', 'C:\BI Projects\YahooFinance\source\BBVA.csv', 'https://es.finance.yahoo.com/quote/BBVA/history?p=BBVA', 1, 'https://query1.finance.yahoo.com/v7/finance/download/BBVA?period1=[periodo_inicial]&dummy1=1537083088&period2=[periodo_final]&dummy2=1568619088&interval=1d&events=history&crumb=UogmSXpOr49', 'BBVA.csv', 'BBVA');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('BTC-EUR', 'BTC-EUR', 'C:\BI Projects\YahooFinance\source\BTC-EUR.csv', 'https://es.finance.yahoo.com/quote/BTC-EUR/history?p=BTC-EUR', 1, 'https://query1.finance.yahoo.com/v7/finance/download/BTC-EUR?period1=[periodo_inicial]&dummy1=1537096132&period2=[periodo_final]&dummy2=1568632132&interval=1d&events=history&crumb=UogmSXpOr49', 'BTC-EUR.csv', 'BTC-EUR');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('CABK', 'CABK', 'C:\BI Projects\YahooFinance\source\CAIXY.csv', 'https://finance.yahoo.com/quote/CAIXY?p=CAIXY&.tsrc=fin-srch', 1, 'https://query1.finance.yahoo.com/v7/finance/download/CAIXY?period1=[periodo_inicial]&dummy1=1537101465&period2=[periodo_final]&dummy2=1568637465&interval=1d&events=history&crumb=UogmSXpOr49', 'CAIXY.csv', 'CaixaBank');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('DAX', 'EGDAXI', 'C:\BI Projects\YahooFinance\source\^GDAXI.csv', 'https://es.finance.yahoo.com/quote/%5EGDAXI/history?p=%5EGDAXI', 1, 'https://query1.finance.yahoo.com/v7/finance/download/%5EGDAXI?period1=[periodo_inicial]&dummy1=1537096283&period2=[periodo_final]&dummy2=1568632283&interval=1d&events=history&crumb=UogmSXpOr49', '^GDAXI.csv', 'DAX');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('ESTX50', 'STOXX50E', 'C:\BI Projects\YahooFinance\source\^STOXX50E.csv', 'https://es.finance.yahoo.com/quote/%5ESTOXX50E/history?p=%5ESTOXX50E', 1, 'https://query1.finance.yahoo.com/v7/finance/download/%5ESTOXX50E?period1=[periodo_inicial]&dummy1=1536842481&period2=[periodo_final]&dummy2=1568378481&interval=1d&events=history&crumb=UogmSXpOr49', '^STOXX50E.csv', 'ESTX50');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('FER', 'FER', 'C:\BI Projects\YahooFinance\source\FER.MC.csv', 'https://finance.yahoo.com/quote/FER.MC/history?p=FER.MC&.tsrc=fin-srch', 1, 'https://query1.finance.yahoo.com/v7/finance/download/FER.MC?period1=[periodo_inicial]&dummy1=1537101465&period2=[periodo_final]&dummy2=1568637465&interval=1d&events=history&crumb=UogmSXpOr49', 'FER.MC.csv', 'Ferrovial');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('GRF', 'GRF', 'C:\BI Projects\YahooFinance\source\GRFS.csv', 'https://finance.yahoo.com/quote/GRFS/history?p=GRFS&.tsrc=fin-srch', 1, 'https://query1.finance.yahoo.com/v7/finance/download/GRFS?period1=[periodo_inicial]&dummy1=1537101465&period2=[periodo_final]&dummy2=1568637465&interval=1d&events=history&crumb=UogmSXpOr49', 'GRFS.csv', 'Grifols');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('IAG', 'IAG', 'C:\BI Projects\YahooFinance\source\IAG.csv', 'https://finance.yahoo.com/quote/IAG/history?p=IAG&.tsrc=fin-srch', 1, 'https://query1.finance.yahoo.com/v7/finance/download/IAG?period1=[periodo_inicial]&dummy1=1537103724&period2=[periodo_final]&dummy2=1568639724&interval=1d&events=history&crumb=UogmSXpOr49', 'IAG.csv', 'IAG');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('IBE', 'IBE', 'C:\BI Projects\YahooFinance\source\IBE.MC.csv', 'https://es.finance.yahoo.com/quote/IBE.MC/history?p=IBE.MC&.tsrc=fin-srch', 1, 'https://query1.finance.yahoo.com/v7/finance/download/IBE.MC?period1=[periodo_inicial]&dummy1=1537101084&period2=[periodo_final]&dummy2=1568637084&interval=1d&events=history&crumb=UogmSXpOr49', 'IBE.MC.csv', 'Iberdrola');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('IBEX 35', 'IBEX 35', 'C:\BI Projects\YahooFinance\source\^IBEX.csv', 'https://es.finance.yahoo.com/quote/%5EIBEX/history?p=%5EIBEX', 1, 'https://query1.finance.yahoo.com/v7/finance/download/%5EIBEX?period1=[periodo_inicial]&dummy1=1537083139&period2=[periodo_final]&dummy2=1568619139&interval=1d&events=history&crumb=UogmSXpOr49', '^IBEX.csv', 'IBEX 35');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('ITX', 'ITX', 'C:\BI Projects\YahooFinance\source\IDEXY.csv', 'https://es.finance.yahoo.com/quote/IDEXY/history?p=IDEXY', 1, 'https://query1.finance.yahoo.com/v7/finance/download/IDEXY?period1=[periodo_inicial]&dummy1=1537101084&period2=[periodo_final]&dummy2=1568637084&interval=1d&events=history&crumb=UogmSXpOr49', 'IDEXY.csv', 'Inditex');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('REE', 'REE', 'C:\BI Projects\YahooFinance\source\REE.MC.csv', 'https://finance.yahoo.com/quote/REE.MC/history?p=REE.MC&.tsrc=fin-srch', 1, 'https://query1.finance.yahoo.com/v7/finance/download/REE.MC?period1=[periodo_inicial]&dummy1=1537101465&period2=[periodo_final]&dummy2=1568637465&interval=1d&events=history&crumb=UogmSXpOr49', 'REE.MC.csv', 'Red Eléctrica Corporación');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('REPSOL', 'REPSOL', 'C:\BI Projects\YahooFinance\source\REP.MC.csv', 'https://es.finance.yahoo.com/quote/REP.MC/history?p=REP.MC', 1, 'https://query1.finance.yahoo.com/v7/finance/download/REP.MC?period1=[periodo_inicial]&dummy1=1537083163&period2=[periodo_final]&dummy2=1568619163&interval=1d&events=history&crumb=UogmSXpOr49', 'REP.MC.csv', 'REPSOL');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('S&P 500', 'GSPC', 'C:\BI Projects\YahooFinance\source\^GSPC.csv', 'https://es.finance.yahoo.com/quote/%5EGSPC/history?p=%5EGSPC', 1, 'https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=[periodo_inicial]&dummy1=1537096468&period2=[periodo_final]&dummy2=1568632468&interval=1d&events=history&crumb=UogmSXpOr49', '^GSPC.csv', 'S&P 500');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('Santand', 'Santand', 'C:\BI Projects\YahooFinance\source\SAN.csv', 'https://es.finance.yahoo.com/quote/SAN/history?p=SAN', 1, 'https://query1.finance.yahoo.com/v7/finance/download/SAN?period1=[periodo_inicial]&dummy1=1537083184&period2=[periodo_final]&dummy2=1568619184&interval=1d&events=history&crumb=UogmSXpOr49', 'SAN.csv', 'Santand');
INSERT INTO files (CodFile, Ticker, Path, URLSource, Enabled, DownloadLink, DownloadedFileName, Description) VALUES ('Telefonica', 'TEF', 'C:\BI Projects\YahooFinance\source\TEF.csv', 'https://es.finance.yahoo.com/quote/TEF/history?p=TEF', 1, 'https://query1.finance.yahoo.com/v7/finance/download/TEF?period1=[periodo_inicial]&dummy1=1537083212&period2=[periodo_final]&dummy2=1568619212&interval=1d&events=history&crumb=UogmSXpOr49', 'TEF.csv', 'Telefonica');