// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request, Response } from "express";
import * as fs from "fs";
import * as path from "path";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00463")
  async BenchmarkTest00463(@Req() req: Request): Promise<unknown> {
    const userInput = (req.body as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(userInput);
    const data: string = readInput();
    const resolved = path.resolve("/var/app/data", data);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const checkedPath = resolved;
    fs.writeFileSync(checkedPath, "data");
    return { created: true };
  }
}
