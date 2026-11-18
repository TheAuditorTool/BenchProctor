import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { dispatchCarrier } from "./carrier_dispatch";
import { summarizeSnapshot } from "./summarize_snapshot";
import { reconcileManifest } from "./reconcile_manifest";
import { resolveRecord } from "./resolve_record";
import { exportRecord } from "./export_record";
import { archiveRoster } from "./archive_roster";
import { buildThreshold } from "./build_threshold";
import { auditReceipt } from "./audit_receipt";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/dispatchCarrier", route(dispatchCarrier));
app.post("/summarizeSnapshot", route(summarizeSnapshot));
app.post("/reconcileManifest", route(reconcileManifest));
app.post("/resolveRecord", route(resolveRecord));
app.post("/exportRecord", route(exportRecord));
app.post("/archiveRoster", route(archiveRoster));
app.post("/buildThreshold", route(buildThreshold));
app.post("/auditReceipt", route(auditReceipt));

app.listen(3000, "0.0.0.0");
