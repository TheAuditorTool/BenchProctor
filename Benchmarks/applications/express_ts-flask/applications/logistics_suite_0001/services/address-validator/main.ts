import express, { Request, Response } from "express";
import session from "express-session";

import { validateAddress } from "./address_validate";
import { summarizeShipment } from "./summarize_shipment";
import { enrichIndex } from "./enrich_index";
import { auditShipment } from "./audit_shipment";
import { verifyCarrier } from "./verify_carrier";
import { rotateLabel } from "./rotate_label";
import { enrichRoster } from "./enrich_roster";
import { collectLabel } from "./collect_label";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/validateAddress", validateAddress);
app.post("/summarizeShipment", summarizeShipment);
app.post("/enrichIndex", enrichIndex);
app.post("/auditShipment", auditShipment);
app.post("/verifyCarrier", verifyCarrier);
app.post("/rotateLabel", rotateLabel);
app.post("/enrichRoster", enrichRoster);
app.post("/collectLabel", collectLabel);

app.listen(3000, "0.0.0.0");
