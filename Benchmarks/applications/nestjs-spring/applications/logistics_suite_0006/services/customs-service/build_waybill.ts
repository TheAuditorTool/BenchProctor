// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("customs-service")
export class BuildWaybill {
  @Post("buildWaybill")
  async buildWaybill(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const consignment: string = readInput();
    return shared.escapeHtml(consignment);
  }
}
