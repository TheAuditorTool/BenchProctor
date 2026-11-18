// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("allocation-service")
export class SolveAllocation {
  @Post("solveAllocation")
  async solveAllocation(@Req() req: Request): Promise<unknown> {
    const headline = req.body.inventory_payload || "";
    net.connect(80, new URL(String(headline)).hostname);
    return { created: true };
  }
}
