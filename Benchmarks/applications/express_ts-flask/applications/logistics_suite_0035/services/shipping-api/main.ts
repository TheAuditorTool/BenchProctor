import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { quoteShipment } from "./shipment_quote";
import { auditWindow } from "./audit_window";
import { collectSummary } from "./collect_summary";
import { reconcileProfile } from "./reconcile_profile";
import { exportProfile } from "./export_profile";
import { mergeLabel } from "./merge_label";
import { verifyManifest } from "./verify_manifest";
import { verifyWindow } from "./verify_window";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/quoteShipment", route(quoteShipment));
app.post("/auditWindow", route(auditWindow));
app.post("/collectSummary", route(collectSummary));
app.post("/reconcileProfile", route(reconcileProfile));
app.post("/exportProfile", route(exportProfile));
app.post("/mergeLabel", route(mergeLabel));
app.post("/verifyManifest", route(verifyManifest));
app.post("/verifyWindow", route(verifyWindow));

app.listen(3000, "0.0.0.0");
