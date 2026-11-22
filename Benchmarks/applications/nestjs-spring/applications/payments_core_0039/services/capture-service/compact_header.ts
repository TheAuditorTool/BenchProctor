// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("capture-service")
export class CompactHeader {
  @Post("compactHeader")
  async compactHeader(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers.host as string) || "";
    const ledger = `${memo}`;
    http.get(ledger);
    return { created: true };
  }
}
