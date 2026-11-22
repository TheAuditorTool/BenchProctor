// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("returns-service")
export class FormatHeader {
  @Post("formatHeader")
  async formatHeader(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(notice);
    const backorder: string = readInput();
    return shared.escapeHtml(backorder);
  }
}
