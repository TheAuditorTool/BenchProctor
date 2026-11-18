import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { acceptWebhook } from "./webhook_accept";
import { reconcileBatch } from "./reconcile_batch";
import { enrichLedger } from "./enrich_ledger";
import { auditRoster } from "./audit_roster";
import { verifyPartner } from "./verify_partner";
import { enrichWebhook } from "./enrich_webhook";
import { reconcileSchedule } from "./reconcile_schedule";
import { publishThreshold } from "./publish_threshold";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/acceptWebhook", route(acceptWebhook));
app.post("/reconcileBatch", route(reconcileBatch));
app.post("/enrichLedger", route(enrichLedger));
app.post("/auditRoster", route(auditRoster));
app.post("/verifyPartner", route(verifyPartner));
app.post("/enrichWebhook", route(enrichWebhook));
app.post("/reconcileSchedule", route(reconcileSchedule));
app.post("/publishThreshold", route(publishThreshold));

app.listen(3000, "0.0.0.0");
