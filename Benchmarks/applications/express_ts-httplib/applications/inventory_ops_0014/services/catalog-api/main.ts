import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { lookupSku } from "./sku_lookup";
import { archiveHeader } from "./archive_header";
import { enrichHeader } from "./enrich_header";
import { loadBatch } from "./load_batch";
import { renderLedger } from "./render_ledger";
import { resolveAllocation } from "./resolve_allocation";
import { rotateDigest } from "./rotate_digest";
import { reconcileSummary } from "./reconcile_summary";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/lookupSku", route(lookupSku));
app.post("/archiveHeader/:id", route(archiveHeader));
app.post("/enrichHeader", route(enrichHeader));
app.post("/loadBatch", route(loadBatch));
app.post("/renderLedger", route(renderLedger));
app.post("/resolveAllocation", route(resolveAllocation));
app.post("/rotateDigest", route(rotateDigest));
app.post("/reconcileSummary", route(reconcileSummary));

app.listen(3000, "0.0.0.0");
