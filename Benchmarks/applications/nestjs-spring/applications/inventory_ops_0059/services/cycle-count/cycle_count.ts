// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("cycle-count")
export class RunCycleCount {
  @Post("runCycleCount")
  async runCycleCount(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers.origin as string) || "";
    const backorder = memo != null ? memo : '';
    await fetch("http://supplier-feed:8080/PullSupplierFeed", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({inventory_payload: backorder})});
    return { created: true };
  }
}
