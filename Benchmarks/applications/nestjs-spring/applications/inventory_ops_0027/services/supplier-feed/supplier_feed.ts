// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("supplier-feed")
export class PullSupplierFeed {
  @Post("pullSupplierFeed")
  async pullSupplierFeed(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const restock: string = transform(summary);
    await fetch("http://allocation-service:8080/SolveAllocation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: restock})});
    return { created: true };
  }
}
