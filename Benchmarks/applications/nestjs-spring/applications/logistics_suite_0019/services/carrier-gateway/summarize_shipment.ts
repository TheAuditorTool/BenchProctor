// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, StreamableFile } from "@nestjs/common";
import { Request } from "express";

@Controller("carrier-gateway")
export class SummarizeShipment {
  @Post("summarizeShipment")
  async summarizeShipment(@Req() req: Request): Promise<unknown> {
    const citation = (req.query.id as string) || "";
    const [parcel] = String(citation).split(',');
    return new StreamableFile(Buffer.from("<section>" + parcel + "</section>"), { type: "text/html; charset=utf-8" });
  }
}
