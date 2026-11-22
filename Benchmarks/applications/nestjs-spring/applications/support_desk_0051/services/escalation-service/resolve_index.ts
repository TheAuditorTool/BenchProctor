// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("escalation-service")
export class ResolveIndex {
  @Post("resolveIndex")
  async resolveIndex(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const grievance: string = readInput();
    return shared.escapeHtml(grievance);
  }
}
