// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Query, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as childProcess from "child_process";
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
  @Post("BenchmarkTest00033")
  async BenchmarkTest00033(@Query("id") id: string): Promise<unknown> {
    const userInput = id || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(userInput);
    const data: string = readInput();
    if (!/^(asc|desc|name|created)$/.test(String(data))) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    childProcess.execSync("echo " + processed);
    return { created: true };
  }
}
