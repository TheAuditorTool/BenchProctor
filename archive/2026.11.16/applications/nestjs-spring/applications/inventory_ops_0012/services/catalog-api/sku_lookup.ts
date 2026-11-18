// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("catalog-api")
export class LookupSku {
  @Post("lookupSku")
  async lookupSku(@Req() req: Request): Promise<unknown> {
    const phrase = (req.query.id as string) || "";
    const backorder = Buffer.from(phrase, "hex").toString();
    await fetch("http://supplier-feed:8080/PullSupplierFeed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
    return { created: true };
  }
}
