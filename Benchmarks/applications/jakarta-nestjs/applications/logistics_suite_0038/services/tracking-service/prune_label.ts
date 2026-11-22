// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("tracking-service")
export class PruneLabel {
  @Post("pruneLabel")
  async pruneLabel(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.origin as string) || "";
    const _raw = wording;
    const consignment = (_raw && _raw.length > 0) ? _raw : 'default';
    const reportSpec = jsYaml.load(String(consignment), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
