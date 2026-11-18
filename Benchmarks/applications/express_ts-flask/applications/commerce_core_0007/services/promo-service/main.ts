import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { applyPromo } from "./promo_apply";
import { loadWindow } from "./load_window";
import { collectManifest } from "./collect_manifest";
import { fetchSummary } from "./fetch_summary";
import { renderReport } from "./render_report";
import { auditLedger } from "./audit_ledger";
import { publishSchedule } from "./publish_schedule";
import { fetchBatch } from "./fetch_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/applyPromo", route(applyPromo));
app.post("/loadWindow", route(loadWindow));
app.post("/collectManifest", route(collectManifest));
app.post("/fetchSummary", route(fetchSummary));
app.post("/renderReport", route(renderReport));
app.post("/auditLedger", route(auditLedger));
app.post("/publishSchedule", route(publishSchedule));
app.post("/fetchBatch", route(fetchBatch));

app.listen(3000, "0.0.0.0");
