import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { openDispute } from "./dispute_open";
import { rotateRoster } from "./rotate_roster";
import { annotateReport } from "./annotate_report";
import { auditLedger } from "./audit_ledger";
import { enrichRoster } from "./enrich_roster";
import { formatWindow } from "./format_window";
import { fetchPolicy } from "./fetch_policy";
import { fetchManifest } from "./fetch_manifest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/openDispute", route(openDispute));
app.post("/rotateRoster", route(rotateRoster));
app.post("/annotateReport", route(annotateReport));
app.post("/auditLedger", route(auditLedger));
app.post("/enrichRoster", route(enrichRoster));
app.post("/formatWindow", route(formatWindow));
app.post("/fetchPolicy", route(fetchPolicy));
app.post("/fetchManifest", route(fetchManifest));

app.listen(3000, "0.0.0.0");
