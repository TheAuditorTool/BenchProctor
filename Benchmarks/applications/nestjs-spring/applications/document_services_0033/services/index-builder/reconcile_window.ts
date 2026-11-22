// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";

@Controller("index-builder")
export class ReconcileWindow {
  @Post("reconcileWindow")
  async reconcileWindow(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.authorization as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(snippet);
    const addendum: string = readInput();
    return shared.escapeHtml(addendum);
  }
}
