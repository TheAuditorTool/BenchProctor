import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { applyWatermark } from "./watermark_apply";
import { annotateReceipt } from "./annotate_receipt";
import { normalizeCaption } from "./normalize_caption";
import { compactManifest } from "./compact_manifest";
import { enrichReport } from "./enrich_report";
import { archiveConfig } from "./archive_config";
import { annotateManifest } from "./annotate_manifest";
import { publishReport } from "./publish_report";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/applyWatermark", route(applyWatermark));
app.post("/annotateReceipt", route(annotateReceipt));
app.post("/normalizeCaption", route(normalizeCaption));
app.post("/compactManifest", route(compactManifest));
app.post("/enrichReport", route(enrichReport));
app.post("/archiveConfig", route(archiveConfig));
app.post("/annotateManifest", route(annotateManifest));
app.post("/publishReport", route(publishReport));

app.listen(3000, "0.0.0.0");
