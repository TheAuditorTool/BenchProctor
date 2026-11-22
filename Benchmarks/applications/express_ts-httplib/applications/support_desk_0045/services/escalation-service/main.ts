import express, { Request, Response } from "express";
import session from "express-session";

import { raiseEscalation } from "./escalation_raise";
import { loadBundle } from "./load_bundle";
import { auditManifest } from "./audit_manifest";
import { annotateSummary } from "./annotate_summary";
import { pruneSummary } from "./prune_summary";
import { enrichTicket } from "./enrich_ticket";
import { resolveTicket } from "./resolve_ticket";
import { reconcileTicket } from "./reconcile_ticket";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/raiseEscalation", raiseEscalation);
app.post("/loadBundle", loadBundle);
app.post("/auditManifest", auditManifest);
app.post("/annotateSummary", annotateSummary);
app.post("/pruneSummary/:id", pruneSummary);
app.post("/enrichTicket", enrichTicket);
app.post("/resolveTicket", resolveTicket);
app.post("/reconcileTicket", reconcileTicket);

app.listen(3000, "0.0.0.0");
