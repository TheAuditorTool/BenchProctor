import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { runSettlement } from "./settlement_batch";
import { enrichManifest } from "./enrich_manifest";
import { loadRecord } from "./load_record";
import { enrichInvoice } from "./enrich_invoice";
import { normalizeSummary } from "./normalize_summary";
import { renderDunning } from "./render_dunning";
import { auditProfile } from "./audit_profile";
import { enrichRecord } from "./enrich_record";

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
app.post("/runSettlement", route(runSettlement));
app.post("/enrichManifest", route(enrichManifest));
app.post("/loadRecord", route(loadRecord));
app.post("/enrichInvoice", route(enrichInvoice));
app.post("/normalizeSummary", route(normalizeSummary));
app.post("/renderDunning", route(renderDunning));
app.post("/auditProfile", route(auditProfile));
app.post("/enrichRecord", route(enrichRecord));

app.listen(3000, "0.0.0.0");
