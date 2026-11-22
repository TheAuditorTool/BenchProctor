import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { postLedgerEntry } from "./ledger_post";
import { mergeReport } from "./merge_report";
import { rotateLedger } from "./rotate_ledger";
import { publishInvoice } from "./publish_invoice";
import { validateReceipt } from "./validate_receipt";
import { fetchInvoice } from "./fetch_invoice";
import { rotateSnapshot } from "./rotate_snapshot";
import { normalizePolicy } from "./normalize_policy";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/postLedgerEntry", route(postLedgerEntry));
app.post("/mergeReport", route(mergeReport));
app.post("/rotateLedger", route(rotateLedger));
app.post("/publishInvoice", route(publishInvoice));
app.post("/validateReceipt", route(validateReceipt));
app.post("/fetchInvoice", route(fetchInvoice));
app.post("/rotateSnapshot", route(rotateSnapshot));
app.post("/normalizePolicy", route(normalizePolicy));

app.listen(3000, "0.0.0.0");
