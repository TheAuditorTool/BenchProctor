import express, { Request, Response } from "express";
import session from "express-session";

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
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/lookupSku", lookupSku);
app.post("/archiveHeader", archiveHeader);
app.post("/enrichHeader", enrichHeader);
app.post("/loadBatch", loadBatch);
app.post("/renderLedger", renderLedger);
app.post("/resolveAllocation", resolveAllocation);
app.post("/rotateDigest", rotateDigest);
app.post("/reconcileSummary/:id", reconcileSummary);

app.listen(3000, "0.0.0.0");
