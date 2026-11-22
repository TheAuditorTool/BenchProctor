// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("decision-log")
export class ResolveWindow {
  @Post("resolveWindow")
  async resolveWindow(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers.referer as string) || "";
    const pending: string[] = String(memo).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const verdict: string = collected.join(',');
    const reportSpec = jsYaml.load(String(verdict), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
