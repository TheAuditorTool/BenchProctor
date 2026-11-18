// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, UsePipes, ValidationPipe } from "@nestjs/common";
import { Response } from "express";
import * as xpath from "xpath";
import * as xmldom from "@xmldom/xmldom";
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

class UserInputDto {
  @IsString()
  payload!: string;
}
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
  @Post("BenchmarkTest00523")
  @UsePipes(new ValidationPipe())
  async BenchmarkTest00523(@Body() dto: UserInputDto): Promise<unknown> {
    const userInput = dto.payload;
    const data = `${userInput}`;
    const _coerced = parseFloat(String(data));
    const parsedNum = _coerced;
    const xmlDoc = new (xmldom.DOMParser)().parseFromString("<users/>", "text/xml");
    xpath.select("//user[name='" + parsedNum + "']", xmlDoc);
    return { created: true };
  }
}
