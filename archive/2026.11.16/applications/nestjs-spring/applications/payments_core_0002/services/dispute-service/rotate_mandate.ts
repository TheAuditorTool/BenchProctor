// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("dispute-service")
export class RotateMandate {
  @Post("rotateMandate")
  async rotateMandate(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers.host as string) || "";
    const ledger = `${subtitle}`;
    http.get(ledger);
    return { created: true };
  }
}
