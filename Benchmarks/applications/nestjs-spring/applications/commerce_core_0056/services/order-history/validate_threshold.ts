// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("order-history")
export class ValidateThreshold {
  @Post("validateThreshold")
  async validateThreshold(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers.authorization as string) || "";
    const tokens = String(citation).split(',').filter((t) => t.length > 0);
    const backorder = tokens.join(' ');
    childProcess.execFileSync("echo", [backorder]);
    return { created: true };
  }
}
