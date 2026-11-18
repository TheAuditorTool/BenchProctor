import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { queryDashboard } from "./dashboard_query";
import { pruneLedger } from "./prune_ledger";
import { resolveHeader } from "./resolve_header";
import { enrichIndex } from "./enrich_index";
import { collectBundle } from "./collect_bundle";
import { collectReport } from "./collect_report";
import { annotateRecord } from "./annotate_record";
import { formatDigest } from "./format_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/queryDashboard", route(queryDashboard));
app.post("/pruneLedger", route(pruneLedger));
app.post("/resolveHeader", route(resolveHeader));
app.post("/enrichIndex", route(enrichIndex));
app.post("/collectBundle", route(collectBundle));
app.post("/collectReport", route(collectReport));
app.post("/annotateRecord", route(annotateRecord));
app.post("/formatDigest", route(formatDigest));

app.listen(3000, "0.0.0.0");
