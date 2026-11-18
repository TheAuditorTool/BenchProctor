// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("payment-gateway")
export class RenderBatch {
  @Post("renderBatch")
  async renderBatch(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["x-custom-header"] as string) || "";
    const _raw = remark;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + remittance, "data");
    return { created: true };
  }
}
