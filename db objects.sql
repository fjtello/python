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


