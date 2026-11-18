import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { routeTicket } from "./ticket_route";
import { enrichMacro } from "./enrich_macro";
import { annotateLedger } from "./annotate_ledger";
import { resolveRoster } from "./resolve_roster";
import { auditSummary } from "./audit_summary";
import { reconcileProfile } from "./reconcile_profile";
import { archiveThreshold } from "./archive_threshold";
import { buildLedger } from "./build_ledger";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/routeTicket", route(routeTicket));
app.post("/enrichMacro", route(enrichMacro));
app.post("/annotateLedger", route(annotateLedger));
app.post("/resolveRoster", route(resolveRoster));
app.post("/auditSummary", route(auditSummary));
app.post("/reconcileProfile", route(reconcileProfile));
app.post("/archiveThreshold", route(archiveThreshold));
app.post("/buildLedger", route(buildLedger));

app.listen(3000, "0.0.0.0");
