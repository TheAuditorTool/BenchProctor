import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { submitInvoice } from "./invoice_intake";
import { verifyLedger } from "./verify_ledger";
import { rotateInvoice } from "./rotate_invoice";
import { archiveIndex } from "./archive_index";
import { validateSummary } from "./validate_summary";
import { loadRoster } from "./load_roster";
import { exportDunning } from "./export_dunning";
import { exportBatch } from "./export_batch";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/submitInvoice", route(submitInvoice));
app.post("/verifyLedger", route(verifyLedger));
app.post("/rotateInvoice", route(rotateInvoice));
app.post("/archiveIndex", route(archiveIndex));
app.post("/validateSummary", route(validateSummary));
app.post("/loadRoster", route(loadRoster));
app.post("/exportDunning", route(exportDunning));
app.post("/exportBatch", route(exportBatch));

app.listen(3000, "0.0.0.0");
