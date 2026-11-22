import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { saveRevision } from "./revision_save";
import { mergeReceipt } from "./merge_receipt";
import { resolveManifest } from "./resolve_manifest";
import { enrichArticle } from "./enrich_article";
import { compactSnapshot } from "./compact_snapshot";
import { resolveHeader } from "./resolve_header";
import { renderRecord } from "./render_record";
import { pruneRevision } from "./prune_revision";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/saveRevision/:id", route(saveRevision));
app.post("/mergeReceipt", route(mergeReceipt));
app.post("/resolveManifest", route(resolveManifest));
app.post("/enrichArticle", route(enrichArticle));
app.post("/compactSnapshot", route(compactSnapshot));
app.post("/resolveHeader", route(resolveHeader));
app.post("/renderRecord", route(renderRecord));
app.post("/pruneRevision", route(pruneRevision));

app.listen(3000, "0.0.0.0");
