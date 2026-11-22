import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { renderPreview } from "./preview_render";
import { renderLedger } from "./render_ledger";
import { loadConfig } from "./load_config";
import { archiveRecord } from "./archive_record";
import { buildLedger } from "./build_ledger";
import { publishArticle } from "./publish_article";
import { validateTaxonomy } from "./validate_taxonomy";
import { buildWindow } from "./build_window";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/renderPreview", route(renderPreview));
app.post("/renderLedger/:id", route(renderLedger));
app.post("/loadConfig", route(loadConfig));
app.post("/archiveRecord", route(archiveRecord));
app.post("/buildLedger", route(buildLedger));
app.post("/publishArticle", route(publishArticle));
app.post("/validateTaxonomy", route(validateTaxonomy));
app.post("/buildWindow", route(buildWindow));

app.listen(3000, "0.0.0.0");
