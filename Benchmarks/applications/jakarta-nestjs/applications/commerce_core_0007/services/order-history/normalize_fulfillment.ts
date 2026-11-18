// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("order-history")
export class NormalizeFulfillment {
  @Post("normalizeFulfillment")
  async normalizeFulfillment(@Req() req: Request): Promise<unknown> {
    const heading = ((req as any).file?.originalname as string) || "";
    let voucher;
    try { voucher = JSON.parse(heading).value || heading; }
    catch (e) { voucher = heading; }
    nodeSerialize.unserialize(voucher);
    return { created: true };
  }
}
