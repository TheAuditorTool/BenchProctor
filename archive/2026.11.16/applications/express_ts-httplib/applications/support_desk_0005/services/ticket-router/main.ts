import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { routeTicket } from "./ticket_route";
import { enrichMacro } from "./enrich_macro";
import { annotateLedger } from "./annotate_ledger";
import { renderMacro } from "./render_macro";
import { enrichDigest } from "./enrich_digest";
import { rotateBundle } from "./rotate_bundle";
import { publishReceipt } from "./publish_receipt";
import { compactBatch } from "./compact_batch";

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
app.post("/renderMacro", route(renderMacro));
app.post("/enrichDigest", route(enrichDigest));
app.post("/rotateBundle", route(rotateBundle));
app.post("/publishReceipt", route(publishReceipt));
app.post("/compactBatch", route(compactBatch));

app.listen(3000, "0.0.0.0");
