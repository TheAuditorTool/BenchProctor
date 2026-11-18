// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("cart-service")
export class CompactManifest {
  @Post("compactManifest")
  async compactManifest(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers["user-agent"] as string) || "";
    let voucher;
    try { voucher = JSON.parse(memo).value || memo; }
    catch (e) { voucher = memo; }
    JSON.parse(voucher);
    return { created: true };
  }
}
