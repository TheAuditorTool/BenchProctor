// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00174")
  async BenchmarkTest00174(@Body("variables") vars: { input?: string }): Promise<unknown> {
    const userInput = (vars?.input as string) || "";
    const transform = (v: string): string => v.trim();
    const data: string = transform(userInput);
    if (!/^(asc|desc|name|created)$/.test(String(data))) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    eval(processed);
    return { created: true };
  }
}
