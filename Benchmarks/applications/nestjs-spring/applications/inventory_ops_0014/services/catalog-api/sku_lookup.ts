// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("catalog-api")
export class LookupSku {
  @Post("lookupSku")
  async lookupSku(@Req() req: Request): Promise<unknown> {
    const excerpt = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(excerpt).split(',').filter((t) => t.length > 0);
    const restock = tokens.join(' ');
    await fetch("http://supplier-feed:8080/PullSupplierFeed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: restock})});
    return { created: true };
  }
}
