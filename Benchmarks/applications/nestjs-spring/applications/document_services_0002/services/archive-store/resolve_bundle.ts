// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("archive-store")
export class ResolveBundle {
  @Post("resolveBundle")
  async resolveBundle(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.referer as string) || "";
    const pending: string[] = String(wording).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const addendum: string = collected.join(',');
    const reportSpec = jsYaml.load(String(addendum), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
