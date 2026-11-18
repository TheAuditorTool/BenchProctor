// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("payment-gateway")
export class RenderSnapshot {
  @Post("renderSnapshot")
  async renderSnapshot(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["user-agent"] as string) || "";
    let remittance;
    try { remittance = JSON.parse(remark).value || remark; }
    catch (e) { remittance = remark; }
    JSON.parse(remittance);
    return { created: true };
  }
}
