import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { quoteShipment } from "./shipment_quote";
import { resolveLedger } from "./resolve_ledger";
import { buildRoster } from "./build_roster";
import { collectBatch } from "./collect_batch";
import { compactShipment } from "./compact_shipment";
import { formatPolicy } from "./format_policy";
import { reconcileShipment } from "./reconcile_shipment";
import { auditManifest } from "./audit_manifest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/quoteShipment", route(quoteShipment));
app.post("/resolveLedger", route(resolveLedger));
app.post("/buildRoster", route(buildRoster));
app.post("/collectBatch", route(collectBatch));
app.post("/compactShipment", route(compactShipment));
app.post("/formatPolicy", route(formatPolicy));
app.post("/reconcileShipment", route(reconcileShipment));
app.post("/auditManifest", route(auditManifest));

app.listen(3000, "0.0.0.0");
